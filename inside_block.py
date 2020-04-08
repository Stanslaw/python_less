from random import randint

def is_inside(polygon, point):

    # Ключ к разгадке - количество точек пересечения луча и всех сторон фигуры
    # если пересечений четное количество - точка находиться вне фигуры
    # для решения надо использовать косое произведение векторов


    def kosoe_proizved(a, b, offset=(0, 0)):
        """
        Функция реализует косое произведение векторов по координатам точек A(1,1) B(2,2) и поправочному коэффициекну
        если обща] точка не ноль
        """
        a = (a[0] - offset[0], a[1] - offset[1])
        b = (b[0] - offset[0], b[1] - offset[1])
        kp = a[0]*b[1] - b[0]*a[1]
        return kp

    def skalarnoe_proizved(a, b, offset=(0, 0)):
        """
        Функция реализует скалярное произведение векторов по координатам точек A(1,1) B(2,2) и поправочному коэффициекну
        если обща] точка не ноль
        """
        a = (a[0] - offset[0], a[1] - offset[1])
        b = (b[0] - offset[0], b[1] - offset[1])
        sp = a[0]*b[0] + a[1]*b[1]
        return sp

    def point_on_the_line(line, point):
        """
        Функция получает на вход координаты двух точек отрезка и точку проверки. Если точка лежит на отрезке
        возвращаем True в противном случае False
        """

        # 1 если точка совпадает с крайней точкой - возвращаем True
        if point in line:
            # print("True")
            return True

        # 2 определяем лежит ли точка на прямой проходящей через точки line, если нет сразу возвращаем False
        A = line[0]
        B = line[1]

        M = point

        print(A, B, M)

        if kosoe_proizved(B, M, A) != 0:
            return False
        elif skalarnoe_proizved(A, B, M) <= 0:
            return True

        return False


    # крайний случай, точка либо совпадает с вершиной - сразу True и не проводим больше никакие рассчеты
    if point in polygon:
        return True


    # Задаем уравнения луча который проходит только через ребра фигуры
    # то есть уравнение прямой на которой нет ни одной вершины фигуры

    # x = sorted(polygon, key=lambda x: x[1])
    # print(x)
    #
    # min_x = min(polygon, key=lambda x: x[0])[0]
    # max_x = max(polygon, key=lambda x: x[0])[0]
    # min_y = min(polygon, key=lambda y: y[1])[1]
    # max_y = max(polygon, key=lambda y: y[1])[1]
    #
    # # print("min X -", min_x)
    #
    # ray = (randint(min_x, max_x), randint(min_y, max_y))
    #
    # n = 0
    # while (ray in polygon) and n < 300:
    #     n += 1
    #     ray = (randint(min_x, max_x), randint(min_y, max_y))
    #     if n == 297:
    #         print("ERROR Ray construct")
    # print("RAY - ", ray)



    # пробегаемся по всем отрезкам по кругу и проверяем их на пересечения с точкой и с лучем от точки

    new_polygon = (*polygon, polygon[0])
    print(new_polygon)

    for i in range(len(new_polygon)-1):
        tar_a = new_polygon[i]
        tar_b = new_polygon[i+1]

        print("line -", tar_a, tar_b, "point - ", point)

        # если точка лежит на одной из поверхностей - сразу принимаем решение что точка внутри фигуры
        if point_on_the_line((tar_a, tar_b), point):
            print("True")
            return True

        # Определяем пересекает ли луч от контрольной точки проходящий через фигуру поверхность


    def ray_and_corner(pol, poi, ra):
        """
        функция принимает две точки прямой и перебирает все точки углов фигуры
        елси хоть один угол лежит на прямой - выводим True
        """

        new_pol = (*pol, pol[0])

        for i in range(len(new_pol) - 1):
            tar_a = new_pol[i]
            tar_b = new_pol[i + 1]

            # print("line -", tar_a, tar_b, "point - ", point)

            # если точка лежит на одной из поверхностей - сразу принимаем решение что точка внутри фигуры
            # if point_on_the_line((tar_a, tar_b), point):
            #     print("True")
            #     return True

        return False


    # изменим логику проверки
    # Выбираем случайную точку далеко за пределами массива 1000, 1000 например и строим чемер нее прямую
    # если прямая пересекает угол - выбираем другую точку

    ray = (randint(-1000, 1000), randint(-1000, 1000))

    n = 0
    while (ray in polygon) and ray_and_corner(polygon, point, ray) and n < 300:
        n += 1
        ray = (randint(-1000, 1000), randint(-1000, 1000))
        if n == 297:
            print("ERROR Ray construct")
    print("RAY - ", ray)


    # если не пересекает ни одной грани - точка вне фигуры
    # если пересекает нечетное количество граней - точка внутри
    # если четное - точка снаружи



    print("False")
    return False





if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    # assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
    #                  (4, 2)) == False, "Second"
    # assert is_inside(((1, 1), (4, 1), (2, 3)),
    #                  (3, 2)) == True, "Third"
    # assert is_inside(((1, 1), (4, 1), (1, 3)),
    #                  (3, 3)) == False, "Fourth"
    # assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
    #                  (4, 3)) == True, "Fifth"
    # assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
    #                  (4, 3)) == False, "Sixth"
    # assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
    #                  (3, 3)) == True, "Seventh"
    # assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
    #                  (4, 3)) == False, "Eighth"
