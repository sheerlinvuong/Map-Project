import xml.etree.ElementTree as ET
tree = ET.parse('square with hole.xml')
root = tree.getroot()
from copy import deepcopy
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

ax = a3.Axes3D(pl.figure())
#bounds given aren't very good but we can use it as a default
for bounds in root.iter('bounds'):
    minlat = float(bounds.get("minlat", default=0))
    maxlat = float(bounds.get("maxlat", default=0))
    minlon = float(bounds.get("minlon", default=0))
    maxlon = float(bounds.get("maxlon", default=0))
#print(minlat, maxlat, minlon, maxlon)

def readNodes( root ):
    nodes = {}
    for node in root.iter('node'):
        node_id = str(node.get("id", default=0))
        node_lon = float(node.get("lon", default=0))
        node_lat = float(node.get("lat", default=0))
        xy = {"lon": node_lon, "lat": node_lat}
        nodes[node_id] = xy
    return nodes
nodes = readNodes(root);

for relation in root.findall('relation'):
    relation_id = relation.get('id', default=0)
    for tag in relation.iter('tag'):
        rel_tag = tag.get('v', default=0)
        if rel_tag == "multipolygon":
            #vtx2 = []
            verts = []
            codes =[]
            for member in relation.iter('member'):
                member_ref = member.get('ref', default=0)
                #print(relation_id, member_type, member_ref)
                vtx2=[]
                for way in root.findall('way'):
                    way_id = way.get('id', default=0)
                    if way_id == member_ref:
                        #print(way_id)
                        for nd in way.iter('nd'):
                            way_ref = nd.get('ref', default=0)
                            vtx2.append([nodes[way_ref]["lon"], nodes[way_ref]["lat"]])
                #print(vtx2)
                n = len(vtx2)
                h = 0.005

                verts.append(vtx2)
                print(verts)
                code = np.ones(n, int) * Path.LINETO
                code[0::n] = Path.MOVETO
                code[n-1::n] = Path.CLOSEPOLY
                codes.append(code)

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

                for i in range(len(vtx[0:n])):
                    wall = [vtx[i], vtx[(i + 1) % n], vtx[(i + 1) % n + n], vtx[i + n]]
                    square = a3.art3d.Poly3DCollection([wall])
                    square.set_color(colors.rgb2hex(sp.rand(4)))
                    ax.add_collection3d(square)

                bot = a3.art3d.Poly3DCollection([vtx[0:n]])
                top = a3.art3d.Poly3DCollection([vtx[n:n * 2]])

                bot.set_color(colors.rgb2hex(sp.rand(4)))
                top.set_color(colors.rgb2hex(sp.rand(4)))
                bot.set_edgecolor('k')
                #ax.add_collection3d(bot)
                #ax.add_collection3d(top)
                # ax.auto_scale_xyz(True,True,True)
                ax.set_xlim(minlon, maxlon)  # long
                ax.set_ylim(minlat, maxlat)  # lat
                ax.set_zlim(0, 0.04)
             #<bounds minlat="51.4736700" minlon="-0.1714700" maxlat="51.4742600" maxlon="-0.1704700"/>
pl.show()