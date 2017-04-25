
from visual.text import *
scene = display(title='Example',
     x=0, y=0, width=800, height=600,
      forward=(0,0,-1), center=(0,0,0), fov=pi/6.0,)

#To improve clarity, create a set of x, y and z axis
x_axis= arrow(pos=(0,0,0), axis=(15,0,0), shaftwidth=0.01, headwidth=0.03, color=color.red)
y_axis= arrow(pos=(0,0,0), axis=(0,15,0), shaftwidth=0.07, headwidth=0.03, color=color.blue)
pos_z_axis= arrow(pos=(0,0,0), axis=(0,0,-15), shaftwidth=0.01, headwidth=0.03)
neg_z_axis= arrow(pos=(0,0,0), axis=(0,0,15), shaftwidth=0.01, headwidth=0.03)

# Create a list of 3D xyz points along
# the perimeter in the xz plane (y=0)

tri = Polygon( [(-2,0), (0,4), (1,0)] )

circ = shapes.circle(pos=(0,1.5), radius=0.8)

straight = [(0,0,0),(0,-1,0)]

semicircle = paths.arc(radius=3, angle2=pi)
#3) Create an extrusion object to extrude your shape along your path. Here we've assigned the "straight" path to the pos attribute, and the "tri" shape to the shape attribute.
extrusion(pos=straight, shape=tri-circ,
          color=color.yellow)