from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig)
x = [0,1,1,0]
y = [0,0,1,1]
z = [0,1,0,1]

print ("hello world") #test git
verts = [zip(x, y,z)]
ax.add_collection3d(PolyCollection(verts),zs=z)
plt.show()