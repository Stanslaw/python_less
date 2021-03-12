from typing import List, Tuple

import itertools
from math import sqrt


def count_chains(circles: List[Tuple[int, int, int]]) -> int:

    # your code here
    print(circles)

    chains = []

    # Формируем список всех возможных комбинаций
    for ones in itertools.combinations(circles, 2):

        # Rr - расстояния между центрами откружностей
        # R - радиус большей окружности
        # r - радиус меньшей окружности

        Rr = sqrt((ones[0][0]-ones[1][0])**2 + (ones[0][1]-ones[1][1])**2)
        R = max([ones[0][2], ones[1][2]])
        r = min([ones[0][2], ones[1][2]])

        # Если квадрат суммы радиусов больше квадратов катетов (по Пифагору) звенья пересекаются либо включены друг в друга
        if R - Rr >= r:
            pass
        elif R + r > Rr:
            # Если мы находим пересекающиеся звенья надо их сравнить с уже имеющимися цепочками и либо добавить новую, либо добавиь звено
            if chains:
                flag_0 = True
                flag_1 = True
                for i in chains:
                    if ones[0] in i:
                        # print("ones_0 = ", ones[0], "i = ", i, "+ ones_1 = ", ones[1])
                        if ones[1] not in i:
                            i.append(ones[1])
                        # print("new_i = ", i)
                        flag_0 = False
                    elif ones[1] in i:
                        # print("ones_1 = ", ones[1], "i = ", i, "+ ones_0 = ", ones[0])
                        if ones[0] not in i:
                            i.append(ones[0])
                        # print("new_i = ", i)
                        flag_1 = False
                if flag_0 and flag_1:
                    chains.append([*ones])

                    # print("+++")
            else:
                chains.append([*ones])

    # Все равно получаются разорванные последовательности. Надо еще раз проверять на вхождение одна в другую.



    # # Добавляем к списку последовательностей одиночные звенья
    # for cir in circles:
    #     # print("cir = ", cir)
    #
    #     if not chains:
    #         chains.append([cir])
    #
    #     flag = True
    #
    #     for i in chains:
    #         # print("i = ", i, "cir = ", cir)
    #         if cir in i:
    #             flag = False
    #     if flag:
    #         chains.append([cir])
    #
    print("\n", "chains = ", chains, "len = ", len(chains))
    return len(chains)


if __name__ == '__main__':
    # print("Example:")
    # print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    # assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    # assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    # assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    # assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    # assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    assert count_chains([[1, 3, 1], [2, 2, 1], [4, 2, 1], [5, 3, 1], [3, 3, 1]]) == 1, 'Olymp'
    print("Coding complete? Click 'Check' to earn cool rewards!")
