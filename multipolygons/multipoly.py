import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

axes = plt.gca()

path = Path([(1,0)      ,(-1,1)     ,(-1,-1)    ,(0,0)         ,(2,2)      ,(2,-2)     ,(-2,-2)    ,(-2,2)     ,(0,0)         ,],#(1,0)      ,(-1,1)     ,(-1,-1)    ,(0,0)         ],
            [Path.MOVETO,Path.LINETO,Path.LINETO,Path.CLOSEPOLY,Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.CLOSEPOLY,])#Path.MOVETO,Path.LINETO,Path.LINETO,Path.CLOSEPOLY])
patch = PathPatch(path)
axes.set_xlim(-3,3)
axes.set_ylim(-3,3)
axes.add_patch(patch)

plt.savefig('example.png')
#plt.close('all')
plt.show()