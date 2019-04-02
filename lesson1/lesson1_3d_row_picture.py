# generate data
import os
from mayavi import mlab
from mayavi.modules.api import GridPlane
from mayavi.core.engine import Engine
from mayavi.tools.show import show
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

def crop_xyz(x, y, z, limit):
    x[x>limit] = np.nan
    x[x<-limit] = np.nan
    y[y>limit] = np.nan
    y[y<-limit] = np.nan
    z[z>limit] = np.nan
    z[z<-limit] = np.nan

def gen_surfaces(e):
#    fig = mlab.figure(size=(800, 800))

    ax_ranges = [-limit, limit, -limit, limit, -limit, limit]
    ax_scale = [1.0, 1.0, 1.0]
    ax_extent = ax_ranges * np.repeat(ax_scale, 2)

    crop_xyz(X1, Y1, Z1, limit)
    crop_xyz(X2, Y2, Z2, limit)
    crop_xyz(X3, Y3, Z3, limit)
    surf1 = mlab.mesh(X1, Y1, Z1, colormap='Blues')
    surf2 = mlab.mesh(X2, Y2, Z2, colormap='Oranges')
    surf3 = mlab.mesh(X3, Y3, Z3, colormap='black-white')
#    v  = mlab.view(-30, 75, 8*limit, [0, 0, 0])
    ol = mlab.outline(surf3, color=(.7, .7, .7), extent=ax_extent)
    ax = mlab.axes(surf3, color=(.7, .7, .7), extent=ax_extent,
              ranges=ax_ranges,
              xlabel='x', ylabel='y', zlabel='z')

#    if transparency:
#        surf3.actor.property.opacity = 0.5
#        surf4.actor.property.opacity = 0.5
#        fig.scene.renderer.use_depth_peeling = 1
    e.add_module(surf1)
    e.add_module(surf2)
    e.add_module(surf3)
    
#    e.add_module(v)
    e.add_module(ol)
    e.add_module(ax)

def gen_grid_plane(e):
    gp1 = GridPlane()
    e.add_module(gp1)
    
    gp2 = GridPlane()
    gp2.grid_plane.axis = 'y'
    gp2.grid_plane.position = 1
    e.add_module(gp2)

    gp3 = GridPlane()
    gp3.grid_plane.axis = 'z'
    gp3.grid_plane.position = limit
    e.add_module(gp3)

e = Engine()
e.start()
e.new_scene()

gen_surfaces(e)
gen_grid_plane(e)

e.current_scene.render()
show()
e.stop()

#mlab.savefig(os.path.basename(__file__).replace(".py", "")+".png")

#mlab.show()
#v2_mayavi(True)

# To install mayavi, the following currently works for me (Windows 10):
#
#   conda create --name mayavi_test_py2 python=2.7 matplotlib mayavi=4.4.0
#    (installs pyqt=4.10.4 mayavi=4.4.0 vtk=5.10.1)
#    * the `use_depth_peeling=1` got no effect. Transparency is not correct.
#    * requires `import pyface.qt` or similar workaround
#
# or
#
#   conda create --name mayavi_test_py3 python=3.6 matplotlib
#   conda activate mayavi_test_py3
#   pip install mayavi
