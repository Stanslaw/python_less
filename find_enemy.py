
def find_enemy(you, dir, enemy):

    # сперва надо научиться определять расстояние от точки до точки.

    def num_char(char):
        """"
        Функция принимает букву алфавита и возврящает ее порядковый номер int
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for idx, val in enumerate(alphabet):
            if val == char.lower():
                return idx

    you_l, you_dg = you[0], you[1]
    en_l, en_dg = enemy[0], enemy[1]

    print("1 - ", abs(int(you_dg) - int(en_dg)))
    print("2 - ", abs(num_char(you_l) - num_char(en_l)))

    if you_l == en_l:
        distance = abs(int(you_dg) - int(en_dg))
    elif you_dg == en_dg:
        distance = abs(int(you_dg) - int(en_dg)) + abs(num_char(you_l) - num_char(en_l))
    else:
        distance = abs(int(you_dg) - int(en_dg)) + abs(num_char(you_l) - num_char(en_l)) - 1

    print("distance - ", distance)









    pass


if __name__ == '__main__':
    assert find_enemy('A1', 'N', 'E3') == ['F', 1], "N-1"
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
