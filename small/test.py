import xml.etree.ElementTree as ET
tree = ET.parse('small.xml')
root = tree.getroot()

import csv

with open("smalltest.csv", "w") as file:
    writer = csv.writer(file, lineterminator='\n', delimiter=',')
    writer.writerow(('way','x','y'))

    for way in root.findall('way'):
            way_id = str(way.get('id', default=0))
            for nd in root.iter('nd'):
                way_ref = str(nd.get('ref', default=0))

                for node in root.iter('node'):
                    node_id = str(node.get("id", default=0))
                    node_lon = float(node.get("lon", default=0))
                    node_lat = float(node.get("lat", default=0))
                    print way_ref
                    #if way_ref = node_id
                        #print node_id
