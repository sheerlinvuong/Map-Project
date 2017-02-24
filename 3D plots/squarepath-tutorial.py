import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

verts = [
    (550, 450),
    (455, 519),
    (491, 631),
    (609, 631),
    (645, 519),
    (550, 450),
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor='C5', lw=2)
ax.add_patch(patch)
ax.set_xlim(300,700)
ax.set_ylim(300,700)
plt.show()