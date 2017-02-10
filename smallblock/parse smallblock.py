import xml.etree.ElementTree as ET
tree = ET.parse('smallblock.xml')
root = tree.getroot()

for node in root.iter('node'):
   print(node.attrib)

