import xml.etree.ElementTree as ET
tree = ET.parse('circle.xml')
root = tree.getroot()

import csv

def readNodes( root ):
    nodes = {}
    for node in root.iter('node'):
        node_id = str(node.get("id", default=0))
        node_lon = float(node.get("lon", default=0))
        node_lat = float(node.get("lat", default=0))
        xy = {"lon": node_lon, "lat": node_lat}
        nodes[node_id] = xy
    return nodes

with open("circle.csv", "w") as file:
    writer = csv.writer(file, lineterminator='\n', delimiter=',', quotechar='|')
    writer.writerow(('way','x','y'))

    nodes = readNodes( root );

    for way in root.findall('way'):
        way_id = way.get('id', default=0)
        for nd in root.iter('nd'):
            way_ref = nd.get('ref', default=0)
            print( way_ref, nodes[way_ref] )
            writer.writerow((way_ref, nodes[way_ref]))
