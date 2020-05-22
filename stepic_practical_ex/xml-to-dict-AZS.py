import xmltodict

fin = open('map3.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
fuel_stations = 0
for nodes in parsedxml["osm"]["node"][:]:
    if "tag" in nodes:
        if isinstance(nodes["tag"], list):
            for tag_i in nodes["tag"]:
                # print(tag_i)
                if tag_i["@k"] == "amenity" and tag_i["@v"] == "fuel":
                    fuel_stations += 1
                    print(tag_i)
        else:
            if nodes["tag"]["@k"] == "amenity" and nodes["tag"]["@v"] == "fuel":
                fuel_stations += 1
                print(nodes["tag"])
        #
        # print(nodes["tag"], end="\n\n")


print(fuel_stations)