from __future__ import division, print_function
from visual import *
import xml.etree.ElementTree as ET
tree = ET.parse('tait building.xml')
#tree = ET.parse('moreton.xml')
root = tree.getroot()

for bounds in root.iter('bounds'):
    minlat = float(bounds.get("minlat", default=0))
    maxlat = float(bounds.get("maxlat", default=0))
    minlon = float(bounds.get("minlon", default=0))
    maxlon = float(bounds.get("maxlon", default=0))
#print(minlat, maxlat, minlon, maxlon)
midx = (minlon + maxlon)/2
midy = (minlat + maxlat)/2
a = maxlon - midx
print (a)
scene = display(title='Example',
     x=0, y=0, range=(a,a,a), fov=pi/4800, center=(midx*0.62 ,0,-midy), background=(1,1,1))

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
        vtxo = []
        vtxi = []
        if rel_tag == "multipolygon":
            multi = 1
            for member in relation.iter('member'):
                member_role = member.get('role', default=0)
                member_ref = member.get('ref', default=0)

                for way in root.findall('way'):
                    way_id = way.get('id', default=0)
                    for tag in way.iter('tag'):
                        way_tag = tag.get('k', default=0)
                        if way_tag == "building":
                            multi = 2

                    if way_id == member_ref and member_role == 'outer':
                        for nd in way.iter('nd'):
                            way_ref = nd.get('ref', default=0)
                            vtxo.append([nodes[way_ref]["lon"], nodes[way_ref]["lat"]])
                    if way_id == member_ref and member_role == 'inner':
                        for nd in way.iter('nd'):
                            way_ref = nd.get('ref', default=0)
                            vtxi.append([nodes[way_ref]["lon"], nodes[way_ref]["lat"]])

        else:
            multi = 0
        #print (multi)
        #print (vtxo)

        #print (vtxi)
        if multi != 0:
        #calculate the scale factor of longitude
            scl = 0.62#cos((vtxo[2][1]*pi)/180)

            s = [(p[0]*scl,-p[1]) for p in vtxo] # get the x and y components scaled
            s2 = [(p[0]*scl, -p[1]) for p in vtxi]
            poly = Polygon(s) - Polygon(s2)
            extrusion(pos=[(0,0,0),(0,0.00025,0)], shape=poly, color=color.orange)

for way in root.findall('way'):
    way_id = way.get('id', default=0)
    for tag in way.iter('tag'):
        way_tag = tag.get('k', default=0)
        vtx = []
        if way_tag == "building" and multi !=2:
            building = 1
            for nd in way.iter('nd'):
                way_ref = nd.get('ref', default=0)
                vtx.append([nodes[way_ref]["lon"], nodes[way_ref]["lat"]])
        else:
            building = 0

        if building == 1:
            #print(vtx)
            g = [(p[0] * 0.62, -p[1]) for p in vtx]
            poly = Polygon(g)
            extrusion(pos=[(0, 0, 0), (0, 0.0002, 0)], shape=poly, color=color.red)