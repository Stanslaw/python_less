
def healthy(grid):

    # Сначала ищем горизонтальные линиии


    hor_lines = [] # массив в котором центры нечетных линий и их длинна

    for row in range(len(grid)):
        n = 0
        for col in range(len(grid[0])):
            # print(grid[row][col])
            if grid[row][col] == 1: # находим единицу и начитаем считать длинну
                n += 1
            elif n != 0: # если единицы кончились и N больше или равен 3 значит это может быть колония
                if n > 0 and n%2 != 0:
                    hor_lines.append([[row, col-(n//2)-1], n]) # находим центральное звено
                n = 0
        if n > 2 and n%2 != 0: # Если строка закончилась и N больше или равен 3 - значит это может быть колония
            hor_lines.append([[row, col-(n//2)], n])

    # print(hor_lines)

    # сортируем фигуры по вертикалям

    ver_lines = sorted(hor_lines, key=(lambda x: x[0][1]))
    # print("\n", ver_lines)

    # Разделяем колонии на отдельные сущности заодно проверяем их на сходимость - длинна равна ширине
    vertikal = ver_lines[0][0][1]
    start_row = ver_lines[0][0][0] - 1
    temp_colony = []
    colonies = []
    for i in ver_lines:
        if (i[0][1] == vertikal) and (i[0][0] == start_row + 1):
            temp_colony.append(i)
            start_row += 1
        else:
            colonies.append(temp_colony)
            temp_colony = []
            temp_colony.append(i)
            vertikal = i[0][1]
            start_row = i[0][0]
    colonies.append(temp_colony)



    for i in colonies:
        print("\n", i)

    return 0, 0 # hearts_of_colonies


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check(result, answers):
        return list(result) in answers

    # check(healthy(((0, 1, 0),
    #                (1, 1, 1),
    #                (0, 1, 0),)), [[1, 1]])
    # check(healthy(((0, 0, 1, 0, 0),
    #                (0, 1, 1, 1, 0),
    #                (0, 0, 1, 0, 0),
    #                (0, 0, 0, 0, 0),
    #                (0, 0, 1, 0, 0),)), [[1, 2]])
    # check(healthy(((0, 0, 1, 0, 0),
    #                (0, 1, 1, 1, 0),
    #                (0, 0, 1, 0, 0),
    #                (0, 0, 1, 0, 0),
    #                (0, 0, 1, 0, 0),)), [[0, 0]])
    check(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
    # check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
    #                (0, 0, 0, 2, 2, 2, 2, 2),
    #                (0, 0, 1, 0, 0, 0, 2, 0),
    #                (0, 1, 1, 1, 0, 0, 2, 0),
    #                (1, 1, 1, 1, 1, 0, 2, 0),
    #                (0, 1, 1, 1, 0, 0, 2, 0),
    #                (0, 0, 1, 0, 0, 0, 2, 0),
    #                (0, 0, 0, 1, 0, 0, 2, 0),
    #                (0, 0, 1, 1, 1, 0, 2, 0),
    #                (0, 1, 1, 1, 1, 1, 0, 0),
    #                (0, 0, 1, 1, 1, 0, 0, 0),
    #                (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])
