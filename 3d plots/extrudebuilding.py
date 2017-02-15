import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

vtx = [
[-3.9498747,51.6399228, 0],
[-3.9498921,51.6399444, 0],
[-3.9500316,51.6399062, 0],
[-3.9500174,51.6398865, 0],
[-3.9500772,51.6398687, 0],
[-3.9500222,51.639793,  0],
[-3.9500048,51.6398013, 0],
[-3.9499913,51.6397796, 0],
[-3.9498572,51.6398138, 0],
[-3.9499042,51.6398795, 0],
[-3.9498532,51.6398945, 0],
[-3.9498747,51.6399228, 0],

[-3.9498747,51.6399228, 1],
[-3.9498921,51.6399444, 1],
[-3.9500316,51.6399062, 1],
[-3.9500174,51.6398865, 1],
[-3.9500772,51.6398687, 1],
[-3.9500222,51.639793,  1],
[-3.9500048,51.6398013, 1],
[-3.9499913,51.6397796, 1],
[-3.9498572,51.6398138, 1],
[-3.9499042,51.6398795, 1],
[-3.9498532,51.6398945, 1],
[-3.9498747,51.6399228, 1],
]

n = 12

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

ax.set_ylim(51.63978,51.63996)
ax.set_xlim(-3.9501, -3.9498)
ax.set_zlim(auto=True)
ax.mouse_init(rotate_btn=1, zoom_btn=3)
pl.show()