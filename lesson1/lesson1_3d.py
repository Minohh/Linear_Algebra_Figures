import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.mplot3d import axes3d

rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

def axesCross(ax):
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")

def set_limit(ax, limit):
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_zlim(-limit, limit)

def crop_xyz(x, y, z, limit):
    x[x>limit] = np.nan
    x[x<-limit] = np.nan
    y[y>limit] = np.nan
    y[y<-limit] = np.nan
    z[z>limit] = np.nan
    z[z<-limit] = np.nan

fig = plt.figure(figsize=(10, 4), dpi=120)
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

limit = 5
set_limit(ax1, limit)
set_limit(ax2, limit)

internal = .1
x = np.arange(-limit, limit+internal, internal)
y = np.arange(-limit, limit+internal, internal)
z = np.arange(-limit, limit+internal, internal)

#2x - y = 0
line1 = lambda x: 2*x
y1 = line1(x)
X1, Z1 = np.meshgrid(x, z)
Y1 = np.repeat(np.reshape(y1, (1, np.size(y1))), np.size(y1), axis=0)

#-x + 2y - z = -1
surface2 = lambda x, y: -x+2*y+1
X2, Y2 = np.meshgrid(x, y)
Z2 = surface2(X2, Y2)

#-3y + 4z = 4
surface3 = lambda x, y: (4+3*y)/4
X3, Y3 = np.meshgrid(x, y)
Z3 = surface3(X3, Y3)

crop_xyz(X1, Y1, Z1, limit)
crop_xyz(X2, Y2, Z2, limit)
crop_xyz(X3, Y3, Z3, limit)
ax1.plot_surface(X1, Y1, Z1, alpha=.6)
ax1.plot_surface(X2, Y2, Z2, alpha=.6)
ax1.plot_surface(X3, Y3, Z3, alpha=.6)

#from mayavi import mlab
#mfig = mlab.figure()
#mlab.surf(X1, Y1, Z1)
#mlab.show()

#line go through surface 1 and surface 2
x12 = x
y12 = line1(x12)
z12 = surface2(x12, y12)

#line go through surface 2 and surface 3
line2 = lambda y, z: 2*y - z + 1
line3 = lambda y: (4+3*y)/4
y23 = y
z23 = line3(y23)
x23 = line2(y23, z23)

#line go through surface 1 and surface 3
x13 = x
y13 = line1(x12)
z13 = line3(y13)

crop_xyz(x12, x12, z12, limit)
crop_xyz(x23, y23, z23, limit)
crop_xyz(x13, y13, z13, limit)
ax1.plot(x12, y12, z12)
ax1.plot(x23, y23, z23)
ax1.plot(x13, y13, z13)

#ax1.text(1, 1, "2x-y=0", color='r')
#ax1.text(-2.5, 1, "-x+2y=3", color='b')
#ax1.text(1, 1.6, "(1,2)", color='k')
#ax1.set_title("row picture", y=-.1)

#Orig = [0, 0]
#V = np.array([[2, -1], [-1, 2], [0, 3]])
#clr = ['r', 'b', 'g']
#ax2.quiver(Orig[0], Orig[1], V[:, 0], V[:, 1], color=clr, angles='xy', scale=1, scale_units='xy')
#ax2.text(2, -1, r"$\begin{bmatrix} 2\\ -1 \end{bmatrix}$", color='r')
#ax2.text(-1.5, 2, r"$\begin{bmatrix}-1\\  2 \end{bmatrix}$", color='b')

#S = np.array([[2, -1], [1,  1]])
#D = np.array([[-1, 2], [-1, 2]])
#ax2.quiver(S[:, 0], S[:, 1], D[:, 0], D[:, 1], color='b', angles='xy', scale=1, scale_units='xy', linestyle='--')
#ax2.text(.4, 2.3, r"$1\begin{bmatrix}2\\ -1\end{bmatrix} + 2\begin{bmatrix}-1\\  2 \end{bmatrix} = \begin{bmatrix}0\\ 3\end{bmatrix}$")
#ax2.set_title("coloum picture", y=-.1)

fig.savefig(os.path.basename(__file__).replace(".py", "")+".png", format='png')
plt.show()
