def color_map(region):

    # 1. We find the boundaries of the matrix so that it is convenient to work with it
    max_row = len(region)
    max_col = len(region[0])

    # 2. We move through the matrix and form a dictionary. The key is the basic element, the value is
    #    all borderline digits.

    margin_data = {}

    def zap(margin_data, x, row, col, flag=True):
        '''Add data to the border elements. Removing copies.'''

        if x == region[row][col]:
            flag = False

        if (flag) and (region[row][col] in margin_data) and (x not in margin_data[region[row][col]]):
            margin_data[region[row][col]] += [x]
        elif (flag) and (region[row][col] not in margin_data):
            margin_data[region[row][col]] = [x]

        return margin_data


    for row in range(max_row):
        for col in range(max_col):

            if row > 0:
                t = region[row-1][col]
                margin_data = zap(margin_data, t, row, col)

            if row < max_row-1:
                b = region[row+1][col]
                margin_data = zap(margin_data, b, row, col)

            if col > 0:
                l = region[row][col-1]
                margin_data = zap(margin_data, l, row, col)

            if col < max_col-1:
                r = region[row][col+1]
                margin_data = zap(margin_data, r, row, col)

    colors = [1, 2, 3, 4]

    # Margin set of this task
    if not margin_data.keys():
        return [1]

    # Set the default monochrome color scheme. Further, when finding collisions, we repaint.
    color_sheme = {}
    for i in range(max(margin_data.keys())+1):
        color_sheme[i] = 1

    # print(color_sheme)
    # print(sorted(margin_data.items()))

    flag = True
    # Going to cicle while color_sheme is in balance. Not any change of color.
    while flag:
        flag = False
        for i, j in sorted(margin_data.items()):
            for k in j:
                if color_sheme[i] == color_sheme[k]:
                    flag = True
                    color_sheme[k] = color_sheme[k]+1
                    if color_sheme[k] == 5:
                        color_sheme[k] = 1

    print(list(color_sheme.values()))

    return list(color_sheme.values())


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
    # assert checker(color_map, (
    #     (1, 1, 1, 2, 1, 1),
    #     (1, 1, 1, 1, 1, 1),
    #     (1, 1, 0, 1, 1, 1),
    #     (1, 0, 0, 0, 1, 1),
    #     (1, 1, 0, 4, 3, 1),
    #     (1, 1, 1, 3, 3, 3),
    #     (1, 1, 1, 1, 3, 5),
    # )), "6 pack"

    assert checker(color_map, (
        (7, 4, 4, 4,),
        (7, 0, 1, 5,),
        (7, 2, 3, 5,),
        (6, 6, 6, 5,),
    )), "6 pack"
