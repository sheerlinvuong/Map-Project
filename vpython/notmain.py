from __future__ import division, print_function
from visual import *
import xml.etree.ElementTree as ET
#tree = ET.parse('charles.xml')
tree = ET.parse('big.xml')
root = tree.getroot()

for bounds in root.iter('bounds'):
    minlat = float(bounds.get("minlat", default=0))
    maxlat = float(bounds.get("maxlat", default=0))
    minlon = float(bounds.get("minlon", default=0))
    maxlon = float(bounds.get("maxlon", default=0))
    break
#print(minlat, maxlat, minlon, maxlon)
midx = (minlon + maxlon)/2
midy = (minlat + maxlat)/2
a = maxlon - midx
b = maxlat - midy
print (b)
scene = display(title='Example',
     x=0, y=0, range=(a,a,a), fov=pi/9600, center=(midx*0.62 ,0,-midy), background=(1,1,1))

def readNodes( root ):
    nodes = {}
    for node in root.iter('node'):
        node_id = str(node.get("id", default=0))
        node_lon = float(node.get("lon", default=0))
        node_lat = float(node.get("lat", default=0))
        xy = {"lon": node_lon, "lat": node_lat}
        nodes[node_id] = xy
    return nodes
nodes = readNodes(root)

def readWays( root ):
    ways = {}
    for way in root.iter( 'way' ):
        way_id = str(way.get("id",default=0))
        ways[way_id] = way
    return ways
ways = readWays( root );

def readRels (root): # don't really need
    rels={}
    for relation in root.iter('relation'):
        rel_id = str(relation.get("id",default=0))
        rels[rel_id] = relation
    return rels
rels = readRels(root);

#for way in root.findall('way'):
#    for tag in way.iter('tag'):
#        tag1 = tag.get('k', default=0)
#
#        if tag1 == "building":
#            for tag in way.iter('tag'):
#                rTag = tag.get('k', default=0)
#                rTag2 = tag.get('v', default=0)
#                if rTag in ("building:levels", "levels", "level"):
#                    #print(float(rTag2))  # sets height if found
#                    v_split = rTag2.split(";")
#                    v = max(v_split)
#                    #print(float(v))

def readBinR (root): #NOT MULTIPOLYGON!
    wp ={}
    for relation in root.findall('relation'):
        #relation_id = relation.get('id', default=0)
        mpfound = 0
        for tag in relation.iter('tag'):
            rel_tag = tag.get('v', default=0)
            if rel_tag == "multipolygon":
                mpfound = 1
                break
        if mpfound == 0:
            for tag in relation.iter('tag'):
                rel_tag2 = tag.get('k', default=0)
                if rel_tag2 == "building":
                    wp[member_ref] = 1
                    for member in relation.iter('member'):
                        member_type = member.get('type', default=0)
                        if member_type == "way":
                            member_ref = member.get('ref', default=0)
                            #wd.append(member_ref)

                    for tag in relation.iter('tag'):       # gets the height
                        rTag = tag.get('k', default=0)
                        rTag2 = tag.get('v', default=0)
                        if rTag in ("building:levels", "levels", "level"):
                            wp[member_ref] = int(rTag2)     #sets height if found

                else:
                    found = 0
                    for member in relation.iter('member'):
                        member_type = member.get('type', default=0)
                        if member_type == "way":
                            member_ref = member.get('ref', default=0)
                            way = ways.get(member_ref, "None")

                            if way != "None":
                                for tag in way.iter('tag'):
                                    wTag = tag.get('k', default=0)
                                    if wTag == 'building':
                                        found = 1
                                        wp[member_ref] = 1
                                        break
                            if found == 1:
                                #wd.append(member_ref)
                                for tag in relation.iter('tag'):  # gets the height
                                    rTag = tag.get('k', default=0)
                                    rTag2 = tag.get('v', default=0)
                                    if rTag in ("building:levels", "levels", "level"):
                                        wp[member_ref] = int(rTag2)  # sets height if found
    #print ("wd2", wd)
    #print("wp", wp)
    return wp

wp = readBinR(root);
print (wp)