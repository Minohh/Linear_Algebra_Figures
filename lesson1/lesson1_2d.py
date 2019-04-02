import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

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

fig = plt.figure(figsize=(10, 4), dpi=120)
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

axesCross(ax1)
axesCross(ax2)
limit = 3
set_limit(ax1, 3)
set_limit(ax2, 3)


line1 = lambda x: 2*x
line2 = lambda x: .5*(x+3)
x = np.arange(-limit, limit, 1)
ax1.plot(x, line1(x), color='r')
ax1.plot(x, line2(x), color='b')
ax1.text(1, 1, "2x-y=0", color='r')
ax1.text(-2.5, 1, "-x+2y=3", color='b')
ax1.text(1, 1.6, "(1,2)", color='k')
ax1.set_title("row picture", y=-.1)

Orig = [0, 0]
V = np.array([[2, -1], [-1, 2], [0, 3]])
clr = ['r', 'b', 'g']
ax2.quiver(Orig[0], Orig[1], V[:, 0], V[:, 1], color=clr, angles='xy', scale=1, scale_units='xy')
ax2.text(2, -1, r"$\begin{bmatrix} 2\\ -1 \end{bmatrix}$", color='r')
ax2.text(-1.5, 2, r"$\begin{bmatrix}-1\\  2 \end{bmatrix}$", color='b')

S = np.array([[2, -1], [1,  1]])
D = np.array([[-1, 2], [-1, 2]])
ax2.quiver(S[:, 0], S[:, 1], D[:, 0], D[:, 1], color='b', angles='xy', scale=1, scale_units='xy', linestyle='--')
ax2.text(.4, 2.3, r"$1\begin{bmatrix}2\\ -1\end{bmatrix} + 2\begin{bmatrix}-1\\  2 \end{bmatrix} = \begin{bmatrix}0\\ 3\end{bmatrix}$")
ax2.set_title("coloum picture", y=-.1)

fig.savefig(os.path.basename(__file__).replace(".py", "")+".png", format='png')
plt.show()
