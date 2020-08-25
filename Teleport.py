def checkio(teleports_string):
    #return any route from 1 to 1 over all points

    # Формируем из текстовой строки граф
    graph = list(map(lambda x: (x[0], x[1]), teleports_string.split(',')))
    graph_2 = {}

    for i, j in graph:
        if i not in graph_2:
            graph_2[i] = set(j)
        else:
            graph_2[i].update(set(j))
        if j not in graph_2:
            graph_2[j] = set(i)
        else:
            graph_2[j].update(set(i))

    # Находим все вершины графа
    for i in range(len(graph)):
        x = graph.pop(0)
        graph.append(x[0])
        graph.append(x[1])

    print(set(graph))
    print('\n', graph_2)


    # Ходим по графу в поисках пути
    def dfs(graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return visited

    print('\n', 'res -', dfs(graph_2, '1'))

    return None

#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    # assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    # assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    # assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"