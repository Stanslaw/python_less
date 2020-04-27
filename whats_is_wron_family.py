
def is_family(tree):

    # Это задача на граф. Необходимо построить граф и проверить условия.
    # 1. каждый элемент связан с первым
    # 2. Нет циклов


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
    print(set(all_people))
    print("___________________")

    # обходим граф по всем вершинам если из первой вершини проходят все остальные
    # считаем что первое условие True


    def dfs(graph, start, flag, visited=set()):
        # if visited is None:
        #     flag = True
        #     visited = set()

        visited.add(start)
        print("Visited -", visited)


        for next in graph[start]:
            if next in visited:
                print(next, visited, "CICLE")
                flag = False

            else:
                if next in graph:
                   dfs(graph, next, flag, visited)
                else:
                    visited.add(next)
                    print("Visited -", visited)

        print("Visited -", visited)
        return [visited, flag]


    # print(tree[0][0])

    for i in graf:
        print(i)
        x, y = dfs(graf, i, True)
        print("FUN - ", sorted(x), sorted(set(all_people)), y)
        if sorted(x) == sorted(set(all_people)):
            break

    # if sorted(x) == sorted(set(all_people)):
    #     print("True", y)
    #
    #     first_u = True


    # если хоть одно условие False - возвращаем False
    return (sorted(x) == sorted(set(all_people))) * y


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

    # assert is_family([["Logan", "Mike"], ["Alexander", "Jack"], ["Jack", "Logan"]]) == True

    print("Looks like you know everything. It is time for 'Check'!")
