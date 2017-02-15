import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

ax = a3.Axes3D(pl.figure())
for i in range(1):
    #vtx = sp.rand(4,3)
    vtx = [
    [550, 450, 350],#0
    [455, 519, 350],#1
    [491, 631, 350],#2
    [609, 631, 350],#3
    [645, 519, 350],#4
        [550, 450, 0],#5
        [455, 519, 0],#6
        [491, 631, 0],#7
        [609, 631, 0],#8
        [645, 519, 0],#9
    ]

    tri = a3.art3d.Poly3DCollection([vtx[0:5]])
    print (vtx[0:5])
    tri2 = a3.art3d.Poly3DCollection([vtx[5:10]])
    print(vtx[5:10])

    tri.set_color(colors.rgb2hex(sp.rand(4)))
    tri.set_edgecolor('k')
    ax.add_collection3d(tri)
    ax.add_collection3d(tri2)
    ax.set_xlim(300, 700)
    ax.set_ylim(300, 700)
    ax.set_zlim(0, 700)
pl.show()