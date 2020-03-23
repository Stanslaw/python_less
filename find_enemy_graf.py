from math import atan2, degrees

def find_enemy(you, dir, enemy):

    # сперва надо научиться определять расстояние от точки до точки.

    def num_char(char):
        """"
        Функция принимает букву алфавита и возврящает ее порядковый номер int
        """
        for idx, val in enumerate(alphabet):
            if val == char.upper():
                return idx

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet.upper()

    you_l, you_dg = you[0], you[1]
    en_l, en_dg = enemy[0], enemy[1]

    # print(type(you_dg))

    idx_you_l = num_char(you_l)
    idx_en_l = num_char(en_l)

    tmp_len_shortest_way = 0
    you_l_2 = you_l + ""
    you_dg_2 = int(you_dg) + 0
    en_l_2 = en_l + ""
    en_dg_2 = int(en_dg) + 0

    while you_l_2 != en_l_2 and you_dg_2 != en_dg_2:

        if num_char(you_l_2) < num_char(en_l_2) and you_dg_2 < en_dg_2: # слева вверх в право вниз
            tmp_len_shortest_way += 1
            if num_char(you_l_2) % 2:
               you_dg_2 += 1
            you_l_2 = alphabet[num_char(you_l_2)+1]
            # print(tmp_len_shortest_way, you_l_2, you_dg_2)

        elif num_char(you_l_2)<num_char(en_l_2) and you_dg_2>en_dg_2: # слева низ в право вверх
            tmp_len_shortest_way += 1
            if not num_char(you_l_2) % 2:
                you_dg_2 -= 1
            you_l_2 = alphabet[num_char(you_l_2) + 1]

        elif num_char(you_l_2)>num_char(en_l_2) and you_dg_2<en_dg_2: # справа вверх в лево вниз
            tmp_len_shortest_way += 1
            if num_char(you_l_2) % 2:
                you_dg_2 += 1
            you_l_2 = alphabet[num_char(you_l_2) - 1]

        elif num_char(you_l_2)>num_char(en_l_2) and you_dg_2>en_dg_2: # справа низ в лево вверх
            tmp_len_shortest_way += 1
            if not num_char(you_l_2) % 2:
                you_dg_2 -= 1
            you_l_2 = alphabet[num_char(you_l_2) - 1]
            # print(tmp_len_shortest_way, you_l_2, you_dg_2)

    print("End of while")
    # print(you_l, you_dg)
    # print(en_l, en_dg)

    if you_l_2 == en_l_2:
        len_shortest_way = abs(you_dg_2 - en_dg_2) + tmp_len_shortest_way
    elif you_dg_2 == en_dg_2:
        len_shortest_way = abs(num_char(you_l_2) - num_char(en_l_2)) + tmp_len_shortest_way



    # Дело за малым, определить в каком секторе от начальной точки стоит конечная

    # Определяем координаты стартовой и конечной точки
    you_axis = (int(you_dg), idx_you_l)
    enemy_axis = (int(en_dg), idx_en_l)

    # Вычисляем тангенс угла наклона прямой  чтобы найти угол между прямой и осью Х через архтангенс
    arctg_cust2 = degrees(atan2(enemy_axis[1] - you_axis[1], enemy_axis[0] - you_axis[0]))

    # Перейдем к азимуту вместо отрицательных углов
    if arctg_cust2 < 0:
        arctg_cust2 += 360

    print("arctg_cust2 - ", arctg_cust2)

    # Поправочные коэффициенты для исходной направленности отличной от N
    azimut = {"N":0, "NE":60, "SE":120, "S":180, "SW":240, "NW":300}
    arctg_cust2 = (arctg_cust2 + azimut[dir]) % 360

    print("arctg_cust2 - ", arctg_cust2)

    # Формируем правило перевода диаргаммы направленности
    # Распространение оказадось нелинейным, для разных расстояний пришлось подгонять диаграмму направленности

    if len_shortest_way > 7:
        if 0 <= arctg_cust2 <= 54 or 306 <= arctg_cust2 <= 360:
            dirrect_enemy = "B"
        elif 54 < arctg_cust2 < 126:
            dirrect_enemy = "R"
        elif 126 < arctg_cust2 < 234:
            dirrect_enemy = "F"
        elif 234 < arctg_cust2 < 306:
            dirrect_enemy = "L"
        else:
            print("ERROR, bad azimut", arctg_cust2)
    elif 1 < len_shortest_way < 7:
        if 0 <= arctg_cust2 <= 45 or 315 <= arctg_cust2 <= 360:
            dirrect_enemy = "B"
        elif 45 < arctg_cust2 < 135:
            dirrect_enemy = "R"
        elif 135 < arctg_cust2 < 225:
            dirrect_enemy = "F"
        elif 225 < arctg_cust2 < 315:
            dirrect_enemy = "L"
        else:
            print("ERROR, bad azimut", arctg_cust2)
    else:
        if 0 <= arctg_cust2 <= 15 or 345 <= arctg_cust2 <= 360:
            dirrect_enemy = "B"
        elif 15 < arctg_cust2 < 165:
            dirrect_enemy = "R"
        elif 165 < arctg_cust2 < 195:
            dirrect_enemy = "F"
        elif 195 < arctg_cust2 < 345:
            dirrect_enemy = "L"
        else:
            print("ERROR, bad azimut", arctg_cust2)


    print(dirrect_enemy, len_shortest_way)

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
    assert find_enemy('A1', 'SW', 'Z9') == ['B', 25], "N-1"
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
