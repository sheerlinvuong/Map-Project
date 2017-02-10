import xml.etree.ElementTree as ET
tree = ET.parse('square.xml')
root = tree.getroot()

import csv

read = open("square.csv", "r") #to save me from opening excel all the time
with open("square.csv", "w") as file:
    writer = csv.writer(file)
#f = open("square.csv", "w")
    for node in root.iter('node'):
        node_id = str(node.get("id", default=0))
        node_lat = str(node.get("lat", default=0))
        node_lon = str(node.get("lon", default=0))
        writer.writerow((node_id, node_lat, node_lon))
    #print(node.attrib) #check if numbers are correct order
    #print("ID = %s , latitude = %s , longitude = %s " %(node_id, node_lat, node_lon) )

#f.close()

    for way in root.findall('way'):
        way_id = str(way.get('id', default=0))
        for nd in root.iter('nd'):
            way_ref = nd.get('ref')
            #print(way_id,way_ref)
            writer.writerow((way_id, way_ref))

print read.read()
read.close()