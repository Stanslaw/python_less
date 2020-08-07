import random

def color_map(region):

    def coloraze(color_matrix, basis, color):

        for row in range(max_row):
            for col in range(max_col):

                if region[row][col] == basis:
                    color_matrix[row][col] = color

        return color_matrix



    # 1. Смотрим исходные данные
    print(region)

    # 2. Формируем цветовую матрицу с монохромным базовым цыетом
    color_matrix = [[1]*len(region)]*len(region[0])
    print(color_matrix)

    # 3. Находим границы матрицы чтобы было удобно с ней работать
    max_row = len(region)
    max_col = len(region[0])

    # 4. Первоначальный базисный элемент от которогу  будем строить цветовую матрицу
    basis = region[0][0]


    # 5. Начинаем пробегать по матрице. Как только находим не базисный элемент красим его в случайный цвет
    #   но в отличный от всех соседей. После передаем в функцию задание перекрасить все элементы этого базиса в
    #   такой же цвет.
    for row in range(max_row):
        for col in range(max_col):

            if region[row][col] != basis:

                fail_color = []
                if row>0:


                color =

                color_matrix = coloraze(color_matrix, region[row][col], color)


            # color_matrix = matrix_walker(color_matrix, row, col, max_row, max_col)

            # print(region[row][col])

    return [1, 1]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    COLORS = (1, 2, 3, 4)
    ERROR_NOT_FOUND = "Didn't find a color for the country {}"
    ERROR_WRONG_COLOR = "I don't know about the color {}"

    def checker(func, region):
        user_result = func(region)
        if not isinstance(user_result, (tuple, list)):
            print("The result must be a tuple or a list")
            return False
        country_set = set()
        for i, row in enumerate(region):
            for j, cell in enumerate(row):
                country_set.add(cell)
                neighbours = []
                if j < len(row) - 1:
                    neighbours.append(region[i][j + 1])
                if i < len(region) - 1:
                    neighbours.append(region[i + 1][j])
                try:
                    cell_color = user_result[cell]
                except IndexError:
                    print(ERROR_NOT_FOUND.format(cell))
                    return False
                if cell_color not in COLORS:
                    print(ERROR_WRONG_COLOR.format(cell_color))
                    return False
                for n in neighbours:
                    try:
                        n_color = user_result[n]
                    except IndexError:
                        print(ERROR_NOT_FOUND.format(n))
                        return False
                    if cell != n and cell_color == n_color:
                        print("Same color neighbours.")
                        return False
        if len(country_set) != len(user_result):
            print("Excess colors in the result")
            return False
        return True
    # assert checker(color_map, (
    #     (0, 0, 0),
    #     (0, 1, 1),
    #     (0, 0, 2),
    # )), "Small"
    # assert checker(color_map, (
    #     (0, 0, 2, 3),
    #     (0, 1, 2, 3),
    #     (0, 1, 1, 3),
    #     (0, 0, 0, 0),
    # )), "4X4"
    assert checker(color_map, (
        (1, 1, 1, 2, 1, 1),
        (1, 1, 1, 1, 1, 1),
        (1, 1, 0, 1, 1, 1),
        (1, 0, 0, 0, 1, 1),
        (1, 1, 0, 4, 3, 1),
        (1, 1, 1, 3, 3, 3),
        (1, 1, 1, 1, 3, 5),
    )), "6 pack"
