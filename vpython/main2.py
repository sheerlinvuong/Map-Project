from __future__ import division, print_function
from visual import *
import xml.etree.ElementTree as ET
#tree = ET.parse('charles.xml')
tree = ET.parse('bush.xml')
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

def readMPB (root): #reads all multipolygons and puts the ones with the building tag into a list
    mpb = {}        # add all the ways found into a list
    wd = []

    # test = root.findall('relation')
    for relation in root.findall('relation'):
        relation_id = relation.get('id', default=0)

        for tag in relation.iter('tag'):
            rel_tag = tag.get('v', default=0)

            if rel_tag == "multipolygon":
                bfound = 0

                # it is nesssary to iter though relation tag again!
                for tag in relation.iter('tag'):
                    rTag = tag.get('k', default=0)

                    if rTag == "building":
                        bfound = 1
                        mpb[relation_id] = 1 #set defualt height to 1

                        for member in relation.iter('member'):
                            member_ref = member.get('ref', default=0)
                            wd.append(member_ref)

                        # it is nesssary to iter though relation tag again!
                        for tag in relation.iter('tag'):
                            rTag = tag.get('k', default=0)
                            rTag2 = tag.get('v', default=0)
                            if rTag in ("building:levels", "levels", "level"):
                                mpb[relation_id] = int(rTag2) #sets height if found

                # if relation has only multipolygon tag but ways have building tag
                if bfound == 0:
                    found = 0
                    for member in relation.iter('member'):
                        member_ref = member.get('ref', default=0)
                        way = ways.get(member_ref, "None")
                        if way != "None":
                            for tag in way.iter('tag'):
                                wTag = tag.get('k', default=0)
                                if wTag == 'building':
                                    found = 1
                                    break
                    if found == 1:
                        for member in relation.iter('member'):
                            member_ref = member.get('ref', default=0)
                            wd.append(member_ref)
                            #print (member_ref)
                            mpb[relation_id]= 1
    return mpb,wd

mpb, wd = readMPB(root)

def drawMPB (root):

    #print("wd", wd)
    # calculate the scale factor of longitude
    scl = 0.62  # cos((vtxo[2][1]*pi)/180)
    for i in mpb:
        #print (i, mpb[i])
        for relation in root.findall('relation'):
            relation_id = relation.get('id', default=0)
            if relation_id == i:
                for member in relation.iter('member'):
                    member_role = member.get('role', default=0)
                    member_ref = member.get('ref', default=0)
                    for way in root.findall('way'):
                        way_id = way.get('id', default=0)
                        vtxo = []
                        vtxi = []
                        if way_id == member_ref and member_role == 'outer':
                            for nd in way.iter('nd'):
                                way_ref = nd.get('ref', default=0)
                                vtxo.append([nodes[way_ref]["lon"], nodes[way_ref]["lat"]])
                            s = [(p[0] * scl, -p[1]) for p in vtxo]  # get the x and y components scaled
                            poly = Polygon(s)

                        if way_id == member_ref and member_role == 'inner':
                            for nd in way.iter('nd'):
                                way_ref = nd.get('ref', default=0)
                                vtxi.append([nodes[way_ref]["lon"], nodes[way_ref]["lat"]])
                            s2 = [(p[0] * scl, -p[1]) for p in vtxi]
                            #print (s2)
                            poly = poly - Polygon(s2)
                extrusion(pos=[(0, 0, 0), (0, mpb[i]* 0.00035, 0)], shape=poly, color=color.orange)

    return mpb
#mpb = drawMPB(root);   #unhashing this draws the multipolygon buildings
print("relation mp" ,mpb)
print("wd1" ,wd)

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
                    for member in relation.iter('member'):
                        member_ref = member.get('ref', default=0)
                        wd.append(member_ref)
                        wp[member_ref] = 1

                        for tag in relation.iter('tag'):       # gets the height
                            rTag = tag.get('k', default=0)
                            rTag2 = tag.get('v', default=0)
                            if rTag in ("building:levels", "levels", "level"):
                                wp[member_ref] = int(rTag2)     #sets height if found

                else:
                    found = 0
                    for member in relation.iter('member'):
                        member_ref = member.get('ref', default=0)
                        way = ways.get(member_ref, "None")
                        if way != "None":
                            for tag in way.iter('tag'):
                                wTag = tag.get('k', default=0)
                                if wTag == 'building':
                                    found = 1
                                    break
                        if found == 1:
                            wd.append(member_ref)
                            wp[member_ref] = 1
    #print ("wd2", wd)
    #print("wp", wp)
    return wd, wp

def readBinW (root):
    wd, wp = readBinR(root);
    for i in ways:
        way = ways.get(i)
        #print(i, way)
        for tag in way.iter('tag'):
            wTag = tag.get('k', default=0)
            if wTag == "building":
                #print("ok")
                found = 0
                for b in wd:
                    if b == i:
                        found =1
                        break
                if found != 1:
                    wd.append(i)
                    #wp.append(i)
    print ("wd2", wd)
    print("wp", wp)
    return wd, wp

def drawB (root):
    wd, wp = readBinW(root);
    # calculate the scale factor of longitude
    scl = 0.62  # cos((vtxo[2][1]*pi)/180)
    for i in wp:
        vtxo=[]
        way = ways.get(i, "None")
        if way != "None":
            for nd in way.iter('nd'):
                way_ref = nd.get('ref', default=0)
                vtxo.append([nodes[way_ref]["lon"], nodes[way_ref]["lat"]])
            s = [(p[0] * scl, -p[1]) for p in vtxo]  # get the x and y components scaled
            poly = Polygon(s)
            extrusion(pos=[(0, 0, 0), (0, 0.00025, 0)], shape=poly, color=color.red)
    return wp
wp = drawB(root);   #unhashing this draws the buildings

print ("wp drawn", wp)