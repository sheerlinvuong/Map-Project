import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

vtx = [
[550, 450],#0
[455, 519],#1
[491, 631],#2
[609, 631],#3
[645, 519],#4
]
n = len(vtx)
h = 350
print (n)

for i in range(len(vtx)):
    vtx0 = []
    vtx0.extend(vtx[i])
    vtx0.extend([0])

for i in range(len(vtx)):
    vtxh = []
    vtxh.extend(vtx[i])
    vtxh.extend([h])

vtx3d = vtx0, vtxh
print (vtx3d)
ax = a3.Axes3D(pl.figure())
for i in range(len(vtx[0:n])):

    wall = [vtx3d[i], vtx3d[(i+1)%n], vtx3d[(i+1)%n +n], vtx3d[i+n]]
    square = a3.art3d.Poly3DCollection([wall])
    square.set_color(colors.rgb2hex(sp.rand(4)))
    ax.add_collection3d(square)
tri = a3.art3d.Poly3DCollection([vtx3d[0:5]])
tri2 = a3.art3d.Poly3DCollection([vtx3d[5:10]])

tri.set_color(colors.rgb2hex(sp.rand(4)))
tri2.set_color(colors.rgb2hex(sp.rand(4)))
tri.set_edgecolor('k')
ax.add_collection3d(tri)
ax.add_collection3d(tri2)

ax.set_xlim(300, 700)
ax.set_ylim(300, 700)
ax.set_zlim(0, 700)

pl.show()