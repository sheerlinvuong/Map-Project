from copy import deepcopy
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp

vtx2 = [
[-0.1778879, 51.4818491],
[-0.1779446, 51.4818514],
[-0.177942, 51.4818764] ,
[-0.1780268, 51.4818797],
[-0.1780363, 51.4817859],
[-0.178044, 51.4817817] ,
[-0.1780449, 51.481773] ,
[-0.1780394, 51.4817691],
[-0.1780288, 51.4817687],
[-0.1780223, 51.4817722],
[-0.1779541, 51.4817696],
[-0.1779498, 51.4818113],
[-0.177892, 51.481809]  ,
[-0.1778879, 51.4818491],
[-0.1777252, 51.4818457],
[-0.1778297, 51.4818508],
[-0.1778344, 51.4818134],
[-0.1778768, 51.4818155],
[-0.1778828, 51.4817674],
[-0.1778446, 51.4817655],
[-0.1777359, 51.4817602],
[-0.1777252, 51.4818457],
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
#ax.auto_scale_xyz(True,True,True)
ax.set_xlim(-0.1780600,-0.1777100 ) #long
ax.set_ylim(51.4817500,51.4818800)     #lat
ax.set_zlim(auto=True)
#ax.grid(False)
#ax.mouse_init(rotate_btn=1, zoom_btn=3)
print(ax.get_ylim())
 #"51.4817500" minlon="-0.1780600" maxlat="51.4818800" maxlon="-0.1777100
pl.show()