from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import Circle
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import art3d
from itertools import product
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d.art3d import pathpatch_2d_to_3d



fig = plt.figure()
ax = fig.gca(projection = '3d') #Create axes

p = Circle((0,0), .2) #Add a circle in the yz plane
ax.add_patch(p)
pathpatch_2d_to_3d(p, z = 0.5, zdir = 'x')
#pathpatch_translate(p, (0, 0.5, 0))

p = Circle((0,0), .2, facecolor = 'r') #Add a circle in the xz plane
ax.add_patch(p)
pathpatch_2d_to_3d(p, z = 0.5, zdir = 'y')
#pathpatch_translate(p, (0.5, 1, 0))

p = Circle((0,0), .2, facecolor = 'g') #Add a circle in the xy plane
ax.add_patch(p)
pathpatch_2d_to_3d(p, z = 0, zdir = 'z')
#pathpatch_translate(p, (0.5, 0.5, 0))

for normal in product((-1, 1), repeat = 3):
    p = Circle((0,0), .2, facecolor = 'y', alpha = .2)
    ax.add_patch(p)
    pathpatch_2d_to_3d(p, z = 0, zdir = normal)
    #pathpatch_translate(p, 0.5)

plt.show()