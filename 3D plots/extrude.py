import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import art3d
import matplotlib.collections as collections
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import pathpatch_2d_to_3d

#from scipy import interpolate

verts = [
    (550, 450, 0),
    (455, 519, 0),
    (491, 631, 0),
    (609, 631, 0 ),
    (645, 519, 0 ),
    (550, 450, 0 ),
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

codes2 = [Path.MOVETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

fig = plt.figure()
ax = fig.gca(projection = '3d')

patch = patches.PathPatch(path, facecolor='C5', lw=2)
ax.add_patch(patch)
pathpatch_2d_to_3d(patch, z = 0, zdir = 'z')

patch = patches.PathPatch(path, facecolor='C4', lw=2)
ax.add_patch(patch)
pathpatch_2d_to_3d(patch, z = 350, zdir = 'z')

#for every cord in vert, path in z direction
#for i in verts:
 #   path2 = Path()
  #  print (i)

ax.set_xlim(300,700)
ax.set_ylim(300,700)
ax.set_zlim(0,700)
plt.show()