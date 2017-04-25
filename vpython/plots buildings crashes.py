from __future__ import division, print_function
from visual import *
import xml.etree.ElementTree as ET
#tree = ET.parse('charles.xml')
tree = ET.parse('covent garden.xml')
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
nodes = readNodes(root);

def readMPB (root):
    mpb = []
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
                        mpb.append(relation_id)
                        for member in relation.iter('member'):
                            member_ref = member.get('ref', default=0)
                            wd.append(member_ref)
                # if relation has only multipolygon tag but ways have building tag
                if bfound == 0:
                    found = 0
                    for member in relation.iter('member'):
                        member_ref = member.get('ref', default=0)
                        way = ways[member_ref]
                        for tag in way.iter( 'tag' ):
                           wTag=tag.get( 'k', default=0 )
                           if wTag == 'building':
                               found =1
                        if found == 1:
                            wd.append(member_ref)
                            mpb.append(relation_id)
    return mpb,wd

def drawMPB (root):
    mpb, wd = readMPB(root);
    # calculate the scale factor of longitude
    scl = 0.62  # cos((vtxo[2][1]*pi)/180)
    for i in mpb:
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

                extrusion(pos=[(0, 0, 0), (0, 0.00025, 0)], shape=poly, color=color.orange)

    return mpb
#mpb = drawMPB(root);   #unhashing this draws the multipolygon buildings

def readBinR (root): #NOT MULTIPOLYGON!
    mpb, wd = readMPB(root);
    wp =[]
    for relation in root.findall('relation'):
        #relation_id = relation.get('id', default=0)
        for tag in relation.iter('tag'):
            rel_tag = tag.get('v', default=0)
            if rel_tag != "multipolygon":
                for tag in relation.iter('tag'):
                    rel_tag2 = tag.get('k', default=0)
                    if rel_tag2 == "building":
                        for member in relation.iter('member'):
                            member_ref = member.get('ref', default=0)
                            wd.append(member_ref)
                            wp.append(member_ref)
                    else:
                        found = 0
                        for member in relation.iter('member'):
                            member_ref = member.get('ref', default=0)
                            for way in root.findall('way'):
                                way_id = way.get('id', default=0)
                                if member_ref == way_id:
                                    for tag in way.iter('tag'):
                                        way_tag = tag.get('k', default=0)
                                        if way_tag == "building":
                                            found = 1
                            if found == 1:
                                wd.append(member_ref)
                                wp.append(member_ref)
    return wd, wp

def readBinW (root):
    wd, wp = readBinR(root);
    for way in root.findall('way'):
        way_id = way.get('id', default=0)
        for tag in way.iter('tag'):
            way_tag = tag.get('k', default=0)
            if way_tag == "building":
                found = 0
                for i in wd:
                    if i == way_id:
                        found =1
                if found != 1:
                    #wd.append(way_id)
                    wp.append(way_id)
    return wd, wp
wd, wp = readBinW(root);
print (wp)
def drawB (root):
    wd, wp = readBinW(root);
    # calculate the scale factor of longitude
    scl = 0.62  # cos((vtxo[2][1]*pi)/180)
    for i in wp:
        vtxo=[]
        for way in root.findall('way'):
            way_id = way.get('id', default=0)
            if way_id == i:
                for nd in way.iter('nd'):
                    way_ref = nd.get('ref', default=0)
                    vtxo.append([nodes[way_ref]["lon"], nodes[way_ref]["lat"]])
                s = [(p[0] * scl, -p[1]) for p in vtxo]  # get the x and y components scaled
                poly = Polygon(s)
                extrusion(pos=[(0, 0, 0), (0, 0.00025, 0)], shape=poly, color=color.red)
    return mpb
#wp = drawB(root);   #unhashing this draws the buildings
