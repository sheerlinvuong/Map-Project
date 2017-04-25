import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
from copy import deepcopy
import mpl_toolkits.mplot3d as a3
from mpl_toolkits.mplot3d.art3d import pathpatch_2d_to_3d
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

#3/03/17
#using tutorial + parse to get the correct verts plot in 2d
#auto add path.moveto ect to vert
#add 3d axis and plot 2d s
#check if walls still work
#merge with holebuilding.py
#couldnt do that lol

vertsin = [
    [-0.06369	,51.497467 ],
    [-0.063552	,51.4974863],
    [-0.0634706	,51.4972426],
    [-0.0636067	,51.4972245],
    [-0.06369	,51.497467 ],
]
vertsout = [
    [-0.0632996	,51.4971861],
    [-0.0634439	,51.4975776],
    [-0.0638554	,51.4975177],
    [-0.0638234	,51.4974265],
    [-0.063717	,51.4971238],
    [-0.0632996	,51.4971861],
    ]

n=len(vertsin)
code = np.ones(n, int) * Path.LINETO
code[0::n] = Path.MOVETO
code[n-1::n] = Path.CLOSEPOLY

n2=len(vertsout)
code2 = np.ones(n2, int) * Path.LINETO
code2[0::n2] = Path.MOVETO
code2[n2-1::n2] = Path.CLOSEPOLY

codes = []
codes.extend(code)
codes.extend(code2)
print(codes)
verts = []
verts.extend(vertsin)
verts.extend(vertsout)
print(verts)

path = Path(verts, codes)

fig = plt.figure()
ax = a3.Axes3D(fig)
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)
pathpatch_2d_to_3d(patch, z = 0, zdir = 'z')

h = 0.2
patch = patches.PathPatch(path, facecolor='pink')
ax.add_patch(patch)
pathpatch_2d_to_3d(patch, z = h, zdir = 'z')

patch = patches.PathPatch(path, facecolor='pink')
ax.add_patch(patch)
pathpatch_2d_to_3d(patch, z = h+0.03, zdir = 'z')
patch = patches.PathPatch(path, facecolor='pink')
ax.add_patch(patch)
pathpatch_2d_to_3d(patch, z = h+0.04, zdir = 'z')

def addvtx0():
    vtx = deepcopy(vertsin)
    vtxh = deepcopy(vertsin)
    for i in range(len(vertsin)):
        a = vtx[i]
        a.append(0)
        b = vtxh[i]
        b.append(h)
        vtx.append(b)
    return vtx

def addvtx02():
    vtx2 = deepcopy(vertsout)
    vtxh2 = deepcopy(vertsout)
    for i in range(len(vertsout)):
        a = vtx2[i]
        a.append(0)
        b = vtxh2[i]
        b.append(h)
        vtx2.append(b)
    return vtx2

vtx = addvtx0()
for i in range(len(vtx[0:n])):
    wall = [vtx[i], vtx[(i + 1) % n], vtx[(i + 1) % n + n], vtx[i + n]]
    square = a3.art3d.Poly3DCollection([wall])
    square.set_color(colors.rgb2hex(sp.rand(4)))
    ax.add_collection3d(square)

vtx2 = addvtx02()
print(vtx2)
for i in range(len(vtx2[0:n2])):
    wall2 = [vtx2[i], vtx2[(i + 1) % n2], vtx2[(i + 1) % n2 + n2], vtx2[i + n2]]
    square2 = a3.art3d.Poly3DCollection([wall2])
    square2.set_color(colors.rgb2hex(sp.rand(4)))
    ax.add_collection3d(square2)

ax.set_xlim(-0.0640300,-0.0632800)
ax.set_ylim(51.4971100,51.4975800)
plt.show()
#"51.4971100" minlon="-0.0640300" maxlat="51.4975800" maxlon="-0.0632800