def check_connection(network, first, second):
    # print(network)
    # print(first)
    # print(second)
    # print('')

    def bfs_paths(graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    graph = {}

    for relation in network:
        a, b = relation.split("-")
        try:
            graph[a].update([b])
        except KeyError:
            graph[a] = set([b])
        try:
            graph[b].update([a])
        except KeyError:
            graph[b] = set([a])

    # print(graph, "\n")
    #
    # print(list(bfs_paths(graph, first, second)))

    return True if list(bfs_paths(graph, first, second)) else False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3") == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
