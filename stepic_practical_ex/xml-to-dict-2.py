import xmltodict

fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)


print(parsedxml["osm"]["node"])