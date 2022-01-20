from typing import List
def useless_flight(schedule: List) -> List:
    # your code here

    print(schedule, end='\n\n')

    def find_all_paths(graph, start, end, path=[], c_sum=[], c_weight=0):
        ''' Функция поиска всех возможных путей в графе между точками '''

        path = path + [start]

        if start == end:
            c_weight_2 = sum(c_sum)
            c_sum = []
            return [[path, c_weight_2]]

        if start not in graph:
            print('-')
            return []

        paths = []
        print("HllYa")
        # c_sum = []

        for node in graph[start]:
            if node[0] not in path:
                c_sum.append(node[1])
                print(c_sum, sum(c_sum), path, node[0])
                newpaths = find_all_paths(graph, node[0], end, path, c_sum, node[1])

                # print("!!!", newpaths)

                for newpath in newpaths:
                    paths.append(newpath)
                    # c_sum = []
        return paths


    graph = {}

    # Формируем двунаправленный граф
    for el in schedule:
        # graph[el[0]] += [el[1]]
        try:
            graph[el[0]] += [(el[1], el[2])]
        except KeyError:
            graph[el[0]] = [(el[1], el[2])]

        try:
            graph[el[1]] += [(el[0], el[2])]
        except KeyError:
            graph[el[1]] = [(el[0], el[2])]

    print(graph, end='\n\n')
    
    print(find_all_paths(graph, 'A', 'C'))

    # closet_flyses = []
    #
    # for idx, el in enumerate(schedule):
    #     cost_not_per = el[2]
    #     path_el = find_all_paths(graph, el[0], el[1])
    #
    #     for i in path_el:
    #         print("i", i)
    #
    #         for j in range(len(i)-1):
    #             print('j', [i[j], i[j+1]])
    #
    #
    #         complex_cost = 1000000000
    #
    #         if cost_not_per > complex_cost:
    #             closet_flyses.append(idx)
    #             break

    return None


if __name__ == '__main__':
  #   print("Example:")
  #   print(useless_flight([['A', 'B', 50],
  # ['B', 'C', 40],
  # ['A', 'C', 100]]))

    # These "asserts" are used for self-checking and not for an auto-testing
  #   assert useless_flight([['A', 'B', 50],
  # ['B', 'C', 40],
  # ['A', 'C', 100]]) == [2]
  #   assert useless_flight([['A', 'B', 50],
  # ['B', 'C', 40],
  # ['A', 'C', 90]]) == []
  #   assert useless_flight([['A', 'B', 50],
  # ['B', 'C', 40],
  # ['A', 'C', 40]]) == []
    assert useless_flight([['A', 'C', 10],
  ['C', 'B', 10],
  ['C', 'E', 10],
  ['C', 'D', 10],
  ['B', 'E', 25],
  ['A', 'D', 20],
  ['D', 'F', 50],
  ['E', 'F', 90]]) == [4, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
