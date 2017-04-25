from __future__ import division, print_function
from visual import *

#To improve clarity, create a set of x, y and z axis
x_axis= arrow(pos=(0,0,0), axis=(15,0,0), shaftwidth=0.01, headwidth=0.03, color=color.red)
y_axis= arrow(pos=(0,0,0), axis=(0,15,0), shaftwidth=0.07, headwidth=0.03, color=color.blue)
pos_z_axis= arrow(pos=(0,0,0), axis=(0,0,-15), shaftwidth=0.01, headwidth=0.03, color=color.green)
neg_z_axis= arrow(pos=(0,0,0), axis=(0,0,15), shaftwidth=0.01, headwidth=0.03)

# Create a list of 3D xyz points along
# the perimeter in the xz plane (y=0)
pts = [(-1,0,1), (1,0,1), (1,0,-1)]
a = paths.arc(pos=(1,0.5), radius=1, angle1=0.5*pi, angle2=1.1*pi)
pts += a.pos # a.pos is the list of points made by paths.arc
pts += [(-1,0,0), (-1,0,1)]

# Create a list of 2D xy points along the perimeter
s = [(p[0],-p[2]) for p in pts] # get the x and -z components

# Convert to a Polygon object
poly = Polygon(s)

extrusion(pos=[(0,0,0),(0,0.6,0)], shape=poly, color=color.orange)

#we get the lon and lat and put the long and -lat for each vert in a list
# then extrude using the y of the second set of brackets