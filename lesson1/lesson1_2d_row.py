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

fig = plt.figure(figsize=(5, 5), dpi=120)
ax1 = fig.add_subplot(1, 1, 1)

axesCross(ax1)
limit = 3
set_limit(ax1, 3)


line1 = lambda x: 2*x
line2 = lambda x: .5*(x+3)
x = np.arange(-limit, limit, 1)
ax1.plot(x, line1(x), color='r')
ax1.plot(x, line2(x), color='b')
ax1.text(1, 1, "2x-y=0", color='r')
ax1.text(-2.5, 1, "-x+2y=3", color='b')
ax1.text(1, 1.6, "(1,2)", color='k')
ax1.set_title("row picture", y=-.1)

fig.savefig(os.path.basename(__file__).replace(".py", "")+".png", format='png')
plt.show()
