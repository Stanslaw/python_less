
def is_family(tree):

    # Это задача на граф. Необходимо построить граф и проверить условия.
    # 1. каждый элемент связан с первым
    # 2. Нет циклов

    print(tree)

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

    for i in graf:
        graf[i] = set(graf[i])

    print(graf)
    print(set(all_people))

    # обходим граф по всем вершинам если из первой вершини проходят все остальные
    # считаем что первое условие True

    def dfs(graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return visited

    # print(tree[0][0])

    print(dfs(graf, tree[0][0]), first_u)

    if dfs(graf, tree[0][0]) == set(all_people):
        first_u = True



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
