from visual import *
a = 0.001
scene = display(title='Example',
     x=0, y=0, range=(a,a,a), fov=pi/4800, center=(-0.0635553*0.63,0,51.4973554)) #center=(-0.0065,0.0005,50.005)

#To improve clarity, create a set of x, y and z axis
#x_axis= arrow(pos=(-0.05,0,50), axis=(15,0,0), shaftwidth=0.01, headwidth=0.03, color=color.red)
#y_axis= arrow(pos=(-0.05,0,50), axis=(0,15,0), shaftwidth=0.01, headwidth=0.03, color=color.blue)
#pos_z_axis= arrow(pos=(-0.05,0,50), axis=(0,0,-15), shaftwidth=0.01, headwidth=0.03)
#neg_z_axis= arrow(pos=(-0.05,0,50), axis=(0,0,15), shaftwidth=0.01, headwidth=0.03)

ptsin = [
        (-0.06369*0.63	,   51.497467 , 0),
        (-0.063552*0.63	,   51.4974863, 0),
        (-0.0634706*0.63,   51.4972426, 0),
        (-0.0636067*0.63,   51.4972245, 0),
        (-0.06369*0.63	,   51.497467 , 0)]
ptsout = [
        (-0.0632996*0.63	,   51.4971861 , 0 ),
        (-0.0634439*0.63	,   51.4975776 , 0 ),
        (-0.0638554*0.63	,   51.4975177 , 0 ),
        (-0.0638234*0.63	,   51.4974265 , 0 ),
        (-0.063717*0.63	,   51.4971238 , 0 ),
        (-0.0632996*0.63	,   51.4971861 , 0 )]

#def midpoint(p1, p2):
#    return Point((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
s = [(p[0],p[1]) for p in ptsin] # get the x and y components
s2 = [(p[0], p[1]) for p in ptsout]
poly = Polygon(s2) - Polygon(s)
extrusion(pos=[(0,0,0),(0,0.0001,0)], shape=poly, color=color.orange)



