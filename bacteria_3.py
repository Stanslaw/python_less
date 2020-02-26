def reserch_colony(colony):
    """"
    Функция проверяет колонию на правильность (ромб)
    Принимаем данные вида:
    [[[2, 2], 1], [[3, 2], 3], [[4, 2], 5], [[5, 2], 3], [[6, 2], 1]]
    Возвращаем:
    True - правильная колония
    False - не правильная колония
    """

    if colony[len(colony) // 2][1] != len(colony):
        return False

    if len(colony) < 2:
        return False

    num_elements = []
    for i in colony: # записываем в отдельный массив данные о количестве единиц
        num_elements.append(i[1])

    # print(num_elements)
    n = 1
    while num_elements:
        if len(num_elements) == 1 and num_elements.pop(0) == n:
            continue
        elif len(num_elements) == 1:
            return False

        if num_elements.pop(0) == num_elements.pop(-1) == n:
            n += 2
        else:
            return False

    # print(n)

    return True


def healthy(grid):

    # Сначала ищем горизонтальные линиии


    hor_lines = [] # массив в котором центры нечетных линий и их длинна

    for row in range(len(grid)):
        n = 0
        for col in range(len(grid[0])):
            # print(grid[row][col])
            if grid[row][col] == 1: # находим единицу и начитаем считать длинну
                n += 1
            elif n != 0: # если единицы кончились и N больше нуля - пишем данные в базу
                if n > 0 and n%2 != 0: # проверяем на нечетность, четных линий быть не может
                    hor_lines.append([[row, col-(n//2)-1], n]) # находим центральное звено
                n = 0
        if n > 2 and n%2 != 0: # Если строка закончилась и N больше или равен 3 - значит это может быть колония
            hor_lines.append([[row, col-(n//2)], n])

    # print(hor_lines)

    if not hor_lines: # Если в матрице не нашлось ни одной колонии
        return [0, 0]

    # сортируем фигуры по вертикалям

    ver_lines = sorted(hor_lines, key=(lambda x: x[0][1]))
    # print("\n", ver_lines)

    # Разделяем колонии на отдельные сущности заодно проверяем их на сходимость - длинна равна ширине
    vertikal = ver_lines[0][0][1]
    start_row = ver_lines[0][0][0] - 1
    temp_colony = []

    colonies = [] # база с разделенными колониями бактерий, осталось проверить правильность формы

    for i in ver_lines:
        if (i[0][1] == vertikal) and (i[0][0] == start_row + 1):
            temp_colony.append(i)
            start_row += 1
        else:
            # Перед добавлением колонии в базу надо проверить ее на равенство горизонтали и вертикали
            # полная проверка колонии в отдельной функции, возвращяет TRUE если все норм
            if reserch_colony(temp_colony):
                colonies.append(temp_colony[len(temp_colony)//2]) # пишем в базу только центральное звено и размер
            # print(temp_colony[len(temp_colony)//2][1], len(temp_colony))
            temp_colony = []
            temp_colony.append(i)
            vertikal = i[0][1]
            start_row = i[0][0]
    if reserch_colony(temp_colony): # чтобы не потерять последнюю колонию приходиться ее записывать в базу после основного цикла
        colonies.append(temp_colony[len(temp_colony)//2])
    # print(temp_colony[len(temp_colony) // 2][1], len(temp_colony))

    if not colonies: # если правильных колоний в матрице нет вовсе - возвращаем [0, 0]
        print([[0, 0]])
        return [0, 0]

    f_colonies = sorted(colonies, key=(lambda x: x[1]), reverse=True)

    while f_colonies[-1][1] != f_colonies[0][1]: # удаляем все колонии не максимальной длинны
        f_colonies.pop(-1)

    result_colony = []

    for i in f_colonies:
        result_colony.append(i[0])

    print(result_colony)

    return result_colony[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check(result, answers):
        return list(result) in answers

    check(healthy(((0, 1, 0),
                   (1, 1, 1),
                   (0, 1, 0),)), [[1, 1]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 0, 0, 0),
                   (0, 0, 1, 0, 0),)), [[1, 2]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),)), [[0, 0]])
    check(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
    check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
                   (0, 0, 0, 2, 2, 2, 2, 2),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (1, 1, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 0, 0, 1, 0, 0, 2, 0),
                   (0, 0, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])

    check(healthy(((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),)), [[0, 0]])
