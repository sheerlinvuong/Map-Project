from __future__ import division, print_function
from visual import *
import xml.etree.ElementTree as ET
tree = ET.parse('tait building - Copy.xml')
#tree = ET.parse('tait building.xml')
root = tree.getroot()

#for bounds in root.iter('bounds'):
#    minlat = float(bounds.get("minlat", default=0))
#    maxlat = float(bounds.get("maxlat", default=0))
#    minlon = float(bounds.get("minlon", default=0))
#    maxlon = float(bounds.get("maxlon", default=0))
##print(minlat, maxlat, minlon, maxlon)
#midx = (minlon + maxlon)/2
#midy = (minlat + maxlat)/2
#a = maxlon - midx
#b = maxlat - midy
#print (b)
#scene = display(title='Example',
#     x=0, y=0, range=(a,a,a), fov=pi/9600, center=(midx*0.62 ,0,midy), background=(1,1,1))

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

def readMPB (root):
    mpb = {}
    wd = []
    for relation in root.findall('relation'):
        relation_id = relation.get('id', default=0)
        for tag in relation.iter('tag'):
            rel_tag = tag.get('v', default=0)
            if rel_tag == "multipolygon":
                bfound = 0
                #it is nesssary to iter though relation tag again!
                for tag in relation.iter('tag'):
                    rel_tag2 = tag.get('k', default=0)
                    if rel_tag2 == "building":
                        bfound = 1
                        for member in relation.iter('member'):
                            member_role = member.get('role', default=0)
                            member_ref = member.get('ref', default=0)
                            mpb[member_ref] = member_role, relation_id
                            wd.append(member_ref)
                # if relation has only multipolygon tag but ways have building tag
                if bfound == 0:
                    for member in relation.iter('member'):
                        member_ref = member.get('ref', default=0)
                        for way in root.findall('way'):
                            way_id = way.get('id', default=0)
                            if member_ref == way_id:
                                for tag in way.iter('tag'):
                                    way_tag = tag.get('k', default=0)
                                    if way_tag == "building":
                                        bfound = 1
                                        member_role = member.get('role', default=0)
                                        member_ref = member.get('ref', default=0)
                                        mpb[member_ref] = member_role, relation_id
                                        wd.append(member_ref)
    return mpb,wd


mpb, wd = readMPB(root);
print (mpb)
print (wd)
for q in mpb:
    print()
