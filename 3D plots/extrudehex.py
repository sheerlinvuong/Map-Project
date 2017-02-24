import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

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
n = 5

ax = a3.Axes3D(pl.figure())
for i in range(len(vtx[0:n])):
    wall = [vtx[i], vtx[(i+1)%n], vtx[(i+1)%n +n], vtx[i+n]]
    square = a3.art3d.Poly3DCollection([wall])
    square.set_color(colors.rgb2hex(sp.rand(4)))
    ax.add_collection3d(square)

bot = a3.art3d.Poly3DCollection([vtx[0:n]])
top = a3.art3d.Poly3DCollection([vtx[n:n*2]])

bot.set_color(colors.rgb2hex(sp.rand(4)))
top.set_color(colors.rgb2hex(sp.rand(4)))
bot.set_edgecolor('k')
ax.add_collection3d(bot)
ax.add_collection3d(top)

ax.set_xlim(300, 700)
ax.set_ylim(300, 700)
ax.set_zlim(0, 700)

pl.show()