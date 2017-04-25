from __future__ import division, print_function
from visual import *
a = 0.003
b= -0.10147575
scene = display(title='Example',
     x=0, y=0, range=(a,a,a), fov=pi/4800, center=(b*0.63 ,0,51.5280306)) #center=(-0.0065,0.0005,50.005)


ptsin = [
    (-0.1017803,	51.5281103),
    (-0.1012752,	51.5282048),
    (-0.1011532,	51.5279521),
    (-0.1015304,	51.5278816),
    (-0.1015509,	51.5279241),
    (-0.1014184,	51.5279489),
    (-0.1013626,	51.5280142),
    (-0.1013976,	51.5280866),
    (-0.1014944,	51.5281199),
    (-0.1016132,	51.5280977),
    (-0.1016594,	51.528052 ),
    (-0.1017444,	51.5280361),
    (-0.1017803,	51.5281103)]

ptsout = [
    (-0.1011326 ,   51.5283837 ),
    (- 0.1013563,    51.5283417),
    (- 0.10183  ,  51.5282529  ),
    (- 0.1020753,    51.5282069),
    (- 0.1019078,    51.5278598),
    (- 0.1018871,    51.5278197),
    (- 0.1018188,    51.5276775),
    (- 0.1015811,    51.527722 ),
    (- 0.1011057,    51.5278112),
    (- 0.1008762,    51.5278543),
    (- 0.1011326,    51.5283837)]


#calculate the scale factor of longitude
scl = cos((ptsout[5][1]*pi)/180)

s = [(p[0]*scl,p[1]) for p in ptsin] # get the x and y components scaled
s2 = [(p[0]*scl, p[1]) for p in ptsout]
print (s2)
poly = Polygon(s2) - Polygon(s)
extrusion(pos=[(0,0,0),(0,0.0005,0)], shape=poly, color=color.orange)

# get the mid point of the outer polygon after it has been scaled
minlat = 99999
maxlat= -99999
minlon = 99999
maxlon = -9999
#def center (verts):
for p in s2:
    if p[0] < minlon:
        minlon = p[0]
    if p[0] > maxlon:
        maxlon = p[0]
    if p[1] < minlat:
        minlat = p[1]
    if p[1] > maxlat:
        maxlat = p[1]

midx = (minlon + maxlon)/2
print (midx)
midy = (minlat + maxlat)/2
print( midy)


#center(ptsout);
#print(midx,midy)