import xmltodict

fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)

all_nodes = len(parsedxml["osm"]["node"])
nodes_with_tag = 0

for nodes in parsedxml["osm"]["node"]:
    if "tag" in nodes:
        print(nodes["tag"], end="\n\n")
        nodes_with_tag += 1
    # print(nodes, end="\n\n")

print(nodes_with_tag, all_nodes-nodes_with_tag)