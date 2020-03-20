from math import atan, atan2, atanh, pi, degrees

def find_enemy(you, dir, enemy):

    # сперва надо научиться определять расстояние от точки до точки.
    # Надо делать граф который сразу формирует звенья с данными направления
    # https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

    def num_char(char):
        """"
        Функция принимает букву алфавита и возврящает ее порядковый номер int
        """
        for idx, val in enumerate(alphabet):
            if val == char.upper():
                return idx


    def graph_import(num, char):
        """"
        Функция принимает координаты точки и возвращает set всех возможных соседей
        """
        tmp = []

        # смотрим на центр и формируем буквы перебора
        if char == alphabet[min(idx_you_l, idx_en_l)] == alphabet[max(idx_you_l, idx_en_l)]:
            char_zone = [char]
        elif char == alphabet[min(idx_you_l, idx_en_l)]:
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
            if num > min(int(you_dg), int(en_dg)):
                # добавляем верхний или нижний недостающий элемент
                tmp.append("".join([char, str(num-1)]))

        # print(dig_zone, char_zone)

        for num_i in dig_zone:
            for char_j in char_zone:
                # записываем только те данные которые имеют неотрицательный префикс и префикс не выходящий за максимальный
                if (max(int(you_dg), int(en_dg)) >= num_i >= min(int(you_dg), int(en_dg))) and [num_i, char_j] != [num, char]:
                    tmp.append("".join([char_j, str(num_i)]))

        return set(tmp)



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

    graph = {}

    for i in range(min(int(you_dg), int(en_dg)), max(int(you_dg), int(en_dg))+1): # перебираем строки - числа от минимального до максимального
        # print("DGT = ", i)
        for j in alphabet[min(idx_you_l, idx_en_l) : max(idx_you_l, idx_en_l)+1]: # столбцы
            # print("ALPHA = ", j)
            graph["".join([j, str(i)])] = graph_import(i, j)
            # print(j, i)


    # print(graph)

    print("______________________")

    # print(list(dfs_paths(graph, you, enemy)))

    shortest_way = shortest_path(graph, you, enemy)

    len_shortest_way = len(shortest_way) - 1 # длинна пути для вывода результата

    print(shortest_way)
    print(len(shortest_way) - 1)



    # Дело за малым, определить в каком секторе от начальной точки стоит конечная

    # Определяем координаты стартовой и конечной точки
    you_axis = (int(you_dg), idx_you_l)
    enemy_axis = (int(en_dg), idx_en_l)

    # Вычисляем тангенс угла наклона прямой  чтобы найти угол между прямой и осью Х через архтангенс
    arctg_cust2 = degrees(atan2(enemy_axis[1] - you_axis[1], enemy_axis[0] - you_axis[0]))

    # Перейдем к азимуту вместо отрицательных углов
    if arctg_cust2 < 0:
        arctg_cust2 += 360

    print(arctg_cust2)

    # Поправочные коэффициенты для исходной направленности отличной от N
    azimut = {"N":0, "NE":60, "SE":120, "S":180, "SW":240, "NW":300}
    arctg_cust2 = (arctg_cust2 + azimut[dir]) % 360



    # if arctg_cust2 > 180:
    #     arctg_cust2 = 180 - (360 - arctg_cust2)


    # Формируем правило перевода диаргаммы направленности

    if 0 <= arctg_cust2 < 30 or 330 < arctg_cust2 <= 360:
        dirrect_enemy = "B"
    elif 30 < arctg_cust2 < 150:
        dirrect_enemy = "R"
    elif 150 < arctg_cust2 < 210:
        dirrect_enemy = "F"
    elif 210 < arctg_cust2 < 330:
        dirrect_enemy = "L"
    else:
        print("ERROR, bad azimut", arctg_cust2)

    # if -30 < arctg_cust2 < 30:
    #     dirrect_enemy = "B"
    # elif 30 < arctg_cust2 < 150:
    #     dirrect_enemy = "R"
    # elif 150 < arctg_cust2 <= 180 or -180 <= arctg_cust2 < -150:
    #     dirrect_enemy = "F"
    # elif -150 < arctg_cust2 < -30:
    #     dirrect_enemy = "L"
    # else:
    #     print("ERROR, bad azimut", arctg_cust2)

    print(dirrect_enemy)

    # print(you_axis, enemy_axis, arctg_cust, angle_from_x_and_line)

    # рисуем табличку для визуализации
    # print("_____________")
    # for i in range(1, 10):
    #     tmp_alpha_visual = []
    #     for j in alphabet:
    #         tmp_alpha_visual.append("".join([j, str(i)]))
    #     print(*tmp_alpha_visual)

    return [dirrect_enemy, len_shortest_way]


if __name__ == '__main__':
    # assert find_enemy('G5', 'N', 'F1') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")
