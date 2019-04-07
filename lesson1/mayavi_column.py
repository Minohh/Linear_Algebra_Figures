# generate data
import os
import numpy as np
from mayavi import mlab

def xyz_edge_grid(xstart, xend, ystart, yend, zstart, zend):
    w = 11
    h = 11
    X1, Y1 = np.mgrid[xstart:xend:w*1j, ystart:yend:h*1j]
    Z1 = np.full((w, h), zstart)
    
    Y2, Z2 = np.mgrid[ystart:yend:w*1j, zstart:zend:h*1j]
    X2 = np.full((w, h), xstart)
    
    X3, Z3 = np.mgrid[xstart:xend:w*1j, zstart:zend:h*1j]
    Y3 = np.full((w, h), ystart)

    mlab.mesh(X1, Y1, Z1, representation='wireframe', color=(1,1,1))
    mlab.mesh(X2, Y2, Z2, representation='wireframe', color=(1,1,1))
    mlab.mesh(X3, Y3, Z3, representation='wireframe', color=(1,1,1))

limit = 4

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

clr = [(0,0,1), (1,0,0), (0,1,0), (0,0,0)]



mlab.figure(size=(800, 800))
xyz_edge_grid(-limit, limit, -limit, limit, -limit, limit)
mlab.view(20, 75, 8*limit, [0, 0, 0])

#vec = mlab.quiver3d(orig, orig, orig, vectors[0], vectors[1], vectors[2], scale_factor=1, color=clr)
for i in range(4):
    mlab.quiver3d(0, 0, 0, vectors[0][i], vectors[1][i], vectors[2][i], scale_factor=1, color=clr[i])
#mlab.outline(vec, color=(.7, .7, .7))

mlab.savefig(os.path.basename(__file__).replace(".py", "")+".png")
mlab.show()
