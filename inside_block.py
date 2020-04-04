from random import randint

def is_inside(polygon, point):

    # Ключь к разгадке - количество точек пересечения луча и всех сторон фигуры
    # если пересечений четное количество - точка находиться вне фигуры
    # для решения надо использовать косое произведение векторов

    # крайний случай, точка либо совпадает с вершиной либо лежит на каком-то отрезке - сразу True

    if point in polygon:
        return True




    # Первым делом надо задать уравнения луча который проходит только через ребра фигуры
    # то есть уравнение прямой на которой нет ни одной вершины фигуры

    x = sorted(polygon, key=lambda x: x[1])
    print(x)
    min_x = min(polygon, key=lambda x: x[0])
    max_x = max(polygon, key=lambda x: x[0])
    min_y = min(polygon, key=lambda y: y[1])
    max_y = max(polygon, key=lambda y: y[1])
    print(min_x[0], max_x[0])
    print(min_y[1], max_y[1])




    return True or False


if __name__ == '__main__':
    # assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
    #                  (2, 2)) == True, "First"
    # assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
    #                  (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
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
