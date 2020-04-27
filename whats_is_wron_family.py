

# делаем граф
graf = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}



print(graf)
print(" ")


def dfs(graph, start, start_prev=None, flag=None, vertex=None):
    if vertex == None:
        vertex = set()
        flag = False

    vertex.add(start)
    # start_prev = start
    print(vertex)

    for ver in graph[start]:
        if ver not in vertex:
            if ver not in graph:
                vertex.add(ver)
            else:
                dfs(graph, ver, start, flag, vertex)

        elif (ver in vertex) and (ver != start_prev):
            print("ver -", ver, "start_prev -", start_prev)
            #если мы пришли в посещенную вершину надо сделать пометку что в графе есть цикл
            flag = True
            print("FLAG", flag)
        else:
            print("ver -", ver, "start_prev -", start_prev)

    return [vertex, flag]


# print("HI")
for i in graf:
    x = dfs(graf, i)
    print("X =", x[0], "flag = ", x[1])
    print("____________________")

