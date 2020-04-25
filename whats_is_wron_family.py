
def is_family(tree):

    # Это задача на граф. Необходимо построить граф и проверить условия.
    # 1. каждый элемент связан с первым
    # 2. Нет циклов

    # print(tree)

    # делаем граф
    graf = {}
    all_people = []

    for i in tree:
        if i[0] not in graf:
            graf[i[0]] = [i[1]]
        else:
            graf[i[0]] += [i[1]]
        all_people.append(i[0])
        all_people.append(i[1])

    for i in set(all_people):
        if i in graf:
            graf[i] = set(graf[i])
        else:
            graf[i] = {}

    print(graf)
    # print(set(all_people))

    # обходим граф по всем вершинам если из первой вершини проходят все остальные
    # считаем что первое условие True

    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            dfs(graph, next, visited)
        return visited

    def dfs_paths(graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    # print(tree[0][0])

    x = dfs(graf, 'Logan')
    print(list(x))

    # if dfs(graf, tree[0][0]) == set(all_people):
    #     first_u = True



    return True


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert is_family([
    #   ['Logan', 'Mike']
    # ]) == True, 'One father, one son'
    # assert is_family([
    #   ['Logan', 'Mike'],
    #   ['Logan', 'Jack']
    # ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    # assert is_family([
    #   ['Logan', 'Mike'],
    #   ['Logan', 'Jack'],
    #   ['Mike', 'Logan']
    # ]) == False, 'Can you be a father to your father?'
    # assert is_family([
    #   ['Logan', 'Mike'],
    #   ['Logan', 'Jack'],
    #   ['Mike', 'Jack']
    # ]) == False, 'Can you be a father to your brother?'
    # assert is_family([
    #   ['Logan', 'William'],
    #   ['Logan', 'Jack'],
    #   ['Mike', 'Alexander']
    # ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
