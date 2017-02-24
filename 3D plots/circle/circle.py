from copy import deepcopy
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

vtx2 = [
[-0.1473056,    51.4535144],
[-0.1473348,    51.4535224],
[-0.1473664,    51.4535244],
[-0.1473975,    51.45352],
[-0.1474248,    51.4535098],
[-0.1474456,    51.4534948],
[-0.1474583,    51.4534749],
[-0.1474596,    51.4534536],
[-0.1474492,    51.4534332],
[-0.1474285,    51.4534162],
[-0.1473997,    51.4534046],
[-0.1473664,    51.4533997],
[-0.1473323,    51.453402],
[-0.1473015,    51.4534114],
[-0.1472776,    51.4534267],
[-0.1472711,    51.4534352],
[-0.147264,     51.4534446],
[-0.1472601,    51.4534643],
[-0.1472663,    51.4534838],
[-0.147282,     51.4535011],
[-0.1473056,    51.4535144],

]
n = len(vtx2)
h = 1

def addvtx0():
    vtx = deepcopy(vtx2)
    vtxh = deepcopy(vtx2)
    for i in range(len(vtx)):
        a = vtx[i]
        a.append(0)
        b = vtxh[i]
        b.append(h)
        vtx.append(b)
    return vtx

vtx = addvtx0();
#print(vtx)

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

ax.set_xlim(-0.1475600,-0.1471600) #long
ax.set_ylim(51.4533500,51.4535400)     #lat
ax.set_zlim(auto=True)
ax.mouse_init(rotate_btn=1, zoom_btn=3)
pl.show()