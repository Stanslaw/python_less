
def is_family(tree):

    # Это задача на граф. Необходимо построить граф и проверить условия.
    # 1. каждый элемент связан с первым
    # 2. Нет циклов

    # print(tree)

    # y = set(["a", "b", "c"])
    # y = y - set("c")
    # print(y)

    # делаем граф
    graf = {}
    all_people = set()

    for i in tree:
        if i[0] not in graf:
            graf[i[0]] = set([i[1]])
        else:
            tmp = graf[i[0]]
            tmp.add(i[1])
            # print(tmp)
            graf[i[0]] = tmp
            
        all_people.update(set([i[0], i[1]]))

    print(graf)
    # print(sorted(set(all_people)))

    # обходим граф по всем вершинам если из первой вершини проходят все остальные
    # считаем что первое условие True


    def dfs(graph, start, visited=None, flag = None):
        if visited is None:
            visited = set()
            flag = True
        visited.add(start)



        for next in graph[start] - visited:
            if next in graph:
               dfs(graph, next, visited)
            else:
                visited.add(next)

            if not graph[start].isdisjoint(visited):
                print("graph[start]", graph[start], "visited", visited)
                flag = False

        return [visited, flag]


    # print(tree[0][0])

    x, y = dfs(graf, str(tree[0][0]))[0], dfs(graf, str(tree[0][0]))[1]
    print("FUN - ", sorted(x))

    if sorted(x) == sorted(set(all_people)):
        print("True", y)

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
    # assert is_family([
    #   ['Logan', 'Mike'],
    #   ['Logan', 'Jack'],
    #   ['Mike', 'Alexander']
    # ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
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
