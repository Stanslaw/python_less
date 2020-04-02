from typing import List, Tuple
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    # your code here

    # print(coords_1)
    # print(coords_2)

    # Для решения задачи необходимо найти углы треугольников
    # Если углы ровны значит треугольники подобны

    def corners_of_triangle(tulp):

        # чтобы устранить деление на ноль перенесем все координаты на 20
        new_tulp = []
        for i in tulp:
            new_tulp.append((i[0]+20, i[1] + 20))

        tulp = new_tulp

        print(tulp)

        KAB = (tulp[1][1] - tulp[0][1]) / (tulp[1][0] - tulp[0][0])
        KBC = (tulp[2][1] - tulp[1][1]) / (tulp[2][0] - tulp[1][0])
        KCA = (tulp[0][1] - tulp[2][1]) / (tulp[0][0] - tulp[2][0])

        # print("KAB = ", KAB)
        # print("KBC = ", KBC)
        # print("KCA = ", KCA)

        TG_A = (KAB -KCA) / (1+KAB*KCA)
        TG_B = (KBC - KAB) / (1 + KBC * KAB)
        TG_C = (KBC - KCA) / (1 + KBC * KCA)

        # print("TG_A = ", TG_A)
        # print("TG_B = ", TG_B)
        # print("TG_C = ", TG_C)

        angles = sorted([TG_A, TG_B, TG_C])

        print(angles)

        return angles


    # Проверяем на равенство тангенсы углов, если равны - возвращаем True

    if corners_of_triangle(coords_1) == corners_of_triangle(coords_2):
        return True
    else:
        return False


if __name__ == '__main__':
    # print("Example:")
    # print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'

