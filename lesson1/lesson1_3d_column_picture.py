# generate data
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

fig = plt.figure(figsize=(5, 4), dpi=120)
ax  = fig.add_subplot(1, 1, 1, projection='3d')

limit = 4
set_limit(ax, limit)

#2x - y = 0
a = np.array([[2, -1, 0]])

#-x + 2y - z = -1
b = np.array([[-1, 2, -1]])

#-3y + 4z = 4
c = np.array([[0, -3, 4]])

# constant
d = np.array([[0, -1, 4]])

v = np.append(a, b, axis=0)
v = np.append(v, c, axis=0)
v = np.append(v, d, axis=0)
vectors = v.T
orig = np.zeros(4)

clr = ['r', 'b', 'g', 'k']
ax.quiver(orig, orig, orig, vectors[0], vectors[1], vectors[2], color=clr, arrowprops=dict(arrowstyle='->', color=clr))

fig.savefig(os.path.basename(__file__).replace(".py", "")+".png", format='png')
plt.show()

