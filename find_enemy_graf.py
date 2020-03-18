
def find_enemy(you, dir, enemy):

    # сперва надо научиться определять расстояние от точки до точки.

    # Надо делать граф который сразу формирует звенья с данными направления
    # https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

    def num_char(char):
        """"
        Функция принимает букву алфавита и возврящает ее порядковый номер int
        """
        # alphabet = "abcdefghijklmnopqrstuvwxyz"

        for idx, val in enumerate(alphabet):
            if val == char.upper():
                return idx


    def graph_import(num, char):
        """"
        Функция принимает координаты точки и возвращает set всех возможных соседей
        """
        tmp = []


        # смотрим на центр и формируем буквы перебора
        if char == alphabet[min(idx_you_l, idx_en_l)]:
            char_zone = [char, alphabet[num_char(char)+1]]
        elif char == alphabet[max(idx_you_l, idx_en_l)]:
            char_zone = [alphabet[num_char(char) - 1], char]
        else:
            char_zone = [alphabet[num_char(char)-1], char, alphabet[num_char(char)+1]]

        # выбираем правильные цифры для правого и левого столбцов в зависимости от четности
        if num_char(char) % 2 == 0:
            dig_zone = [num-1, num]
            if num < max(int(you_dg), int(en_dg)):
                # добавляем верхний или нижний недостающий элемент
                tmp.append("".join([char, str(num+1)]))
        else:
            dig_zone = [num, num+1]
            if num > 1:
                # добавляем верхний или нижний недостающий элемент
                tmp.append("".join([char, str(num-1)]))


        for num_i in dig_zone:
            for char_j in char_zone:
                # записываем только те данные которые имеют неотрицательный префикс и префикс не выходящий за максимальный
                if max(int(you_dg), int(en_dg)) >= num_i > 0 and [num_i, char_j] != [num, char]:
                    tmp.append("".join([char_j, str(num_i)]))



        return set(tmp)



    def dfs_paths(graph, start, goal):
    # перебираем граф в поисках путей между точками
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    def bfs_paths(graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def shortest_path(graph, start, goal):
        try:
            return next(bfs_paths(graph, start, goal))
        except StopIteration:
            return None




    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet.upper()

    you_l, you_dg = you[0], you[1]
    en_l, en_dg = enemy[0], enemy[1]

    idx_you_l = num_char(you_l)
    idx_en_l = num_char(en_l)

    # if you_l == en_l:
    #     distance = abs(int(you_dg) - int(en_dg))

    graph = {}

    for i in range(min(int(you_dg), int(en_dg)), max(int(you_dg), int(en_dg))+1): # перебираем строки - числа от минимального до максимального
        for j in alphabet[min(idx_you_l, idx_en_l) : max(idx_you_l, idx_en_l)+1]: # столбцы
            graph["".join([j, str(i)])] = graph_import(i, j)
            # print(j, i)


    print(graph)

    print("______________________")

    # print(list(dfs_paths(graph, you, enemy)))


    print(shortest_path(graph, you, enemy))




    pass


if __name__ == '__main__':
    assert find_enemy('B1', 'N', 'D4') == ['F', 1], "N-1"
    # assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    # assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    # assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    # assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    # assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    # assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    # assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    # assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    # assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    # print("You are good to go!")
