from math import sqrt
from typing import List, Tuple
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    # your code here

    # print(coords_1)
    # print(coords_2)


    # Сначала определяем длинны сторон треугольника ABC, если коэффициент подобия ко всем сторонам одинаков -
    # треугольники подобны

    def len_triangle(coor):
        """
        Вычисляем стороны треугодьника, на вход координаты, а выходе - стороны
        """

        AB = sqrt((coor[0][0] - coor[1][0])**2 + (coor[0][1] - coor[1][1])**2)
        AC = sqrt((coor[0][0] - coor[2][0]) ** 2 + (coor[0][1] - coor[2][1]) ** 2)
        BC = sqrt((coor[1][0] - coor[2][0]) ** 2 + (coor[1][1] - coor[2][1]) ** 2)

        return sorted([AB, AC, BC])


    x = len_triangle(coords_1)
    y = len_triangle(coords_2)

    print(x)
    print(y)
    # print(k)


    if x[0]/y[0] == x[1]/y[1] == x[2]/y[2]:
        return True
    else:
        return False




if __name__ == '__main__':
    # print("Example:")
    # print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangels([[-2,-4],[-1,2],[2,1]],[[8,2],[-7,-10],[-10,-1]]) is True, 'basic'

    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
