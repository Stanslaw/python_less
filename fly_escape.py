def escape(jar, fly):
    W, H, d = jar
    x0, y0, vx, vy = fly


    # блок функций скалярного и косого произведений

    def kosoe_proizved(a, b, offset=(0, 0)):
        """
        Функция реализует косое произведение векторов по координатам точек A(1,1) B(2,2) и поправочному коэффициекну
        если общая точка не ноль
        """
        a = (a[0] - offset[0], a[1] - offset[1])
        b = (b[0] - offset[0], b[1] - offset[1])
        kp = a[0]*b[1] - b[0]*a[1]
        return kp

    def skalarnoe_proizved(a, b, offset=(0, 0)):
        """
        Функция реализует скалярное произведение векторов по координатам точек A(1,1) B(2,2) и поправочному коэффициекну
        если общая точка не ноль
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

        # print(A, B, M)

        if kosoe_proizved(B, M, A) != 0:
            return False
        elif skalarnoe_proizved(A, B, M) <= 0:
            return True

        return False

    def point_on_the_ray (start_ray, center_ray, point):
        """"
        Функция принимает точку старта луча, точку продолжения луча, точку проверки
        Если точка проверки лежит на луче - возвращаем True
        """

        if (kosoe_proizved(center_ray, point, start_ray) == 0) and (skalarnoe_proizved(center_ray, point, start_ray) >= 0):
            return True
        else:
            return False



    # Назначаем всем сущностям координаты

    wall_0 = ((0, 0), (0, H))
    wall_1 = ((0, H), ((W-d)/2, H))
    wall_2 = (((W-d)/2, H), ((W+d)/2, H))
    wall_3 = (((W+d)/2, H), (W, H))
    wall_4 = ((W, H), (W, 0))
    wall_5 = ((W, 0), (0, 0))

    walls = [wall_0, wall_1, wall_2, wall_3, wall_4, wall_5]

    for idx, val in enumerate(walls):
        print(f"Wall_{idx} = ", val)

    fly_start = ((x0, y0), (x0+vx, y0+vy))

    print("Fly ray =", fly_start)




    # Теперь стартуем в цикле. Если за 20 итераций луч мухи не пересекает wall_3 - возвращаем False.
    # Как только пересекаем - True

    n=0
    while n<20:
        print(n)




        n+=1


    return False


if __name__ == '__main__':
    # print("Example:")
    # print(escape([1000, 1000, 200], [0, 0, 100, 0]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    # assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    # assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    # assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    # assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"
    print("Coding complete? Click 'Check' to earn cool rewards!")