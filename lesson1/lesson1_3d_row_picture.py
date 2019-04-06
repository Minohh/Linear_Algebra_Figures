# generate data
import os
from mayavi import mlab
import numpy as np

limit = 5
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

# A fix for "API 'QString' has already been set to version 1"
# see https://github.com/enthought/pyface/issues/286#issuecomment-335436808
from sys import version_info
if version_info[0] < 3:
    import pyface.qt

def xyz_edge_grid(xstart, xend, ystart, yend, zstart, zend):
    w = 11
    h = 11
    X1, Y1 = np.mgrid[xstart:xend:w*1j, ystart:yend:h*1j]
    Z1 = np.full((w, h), zstart)
    
    Y2, Z2 = np.mgrid[ystart:yend:w*1j, zstart:zend:h*1j]
    X2 = np.full((w, h), xstart)
    
    X3, Z3 = np.mgrid[xstart:xend:w*1j, zstart:zend:h*1j]
    Y3 = np.full((w, h), ystart)

    mlab.mesh(X1, Y1, Z1, representation='wireframe')
    mlab.mesh(X2, Y2, Z2, representation='wireframe')
    mlab.mesh(X3, Y3, Z3, representation='wireframe')

def crop_xyz(x, y, z, limit):
    x[x>limit] = np.nan
    x[x<-limit] = np.nan
    y[y>limit] = np.nan
    y[y<-limit] = np.nan
    z[z>limit] = np.nan
    z[z<-limit] = np.nan

def gen_surfaces():
    mlab.figure(size=(800, 800))
    xyz_edge_grid(-limit, limit, -limit, limit, -limit, limit)

    ax_ranges = [-limit, limit, -limit, limit, -limit, limit]
    ax_scale = [1.0, 1.0, 1.0]
    ax_extent = ax_ranges * np.repeat(ax_scale, 2)

    crop_xyz(X1, Y1, Z1, limit)
    crop_xyz(X2, Y2, Z2, limit)
    crop_xyz(X3, Y3, Z3, limit)
    surf1 = mlab.mesh(X1, Y1, Z1, colormap='Blues')
    surf2 = mlab.mesh(X2, Y2, Z2, colormap='Oranges')
    surf3 = mlab.mesh(X3, Y3, Z3, colormap='black-white')
    mlab.view(-30, 75, 8*limit, [0, 0, 0])
    mlab.outline(surf3, color=(.7, .7, .7), extent=ax_extent)
    #mlab.axes(surf3, color=(.7, .7, .7), extent=ax_extent,
    #          ranges=ax_ranges,
    #          xlabel='x', ylabel='y', zlabel='z')


gen_surfaces()

mlab.savefig(os.path.basename(__file__).replace(".py", "")+".png")
mlab.show()

