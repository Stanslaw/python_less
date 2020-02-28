def wall_keeper(on_panels):

    def switch_light_panel(row, col):
        """
        Функция получает на вход координаты световой ячейки и переключает ячейку чтобы ее выключить.
        Возвращаем номер тумблера который нажимаем.
        """
        wall_matrix[row][col][1] = not wall_matrix[row][col][1]

        if row > 0:
            wall_matrix[row-1][col][1] = not wall_matrix[row-1][col][1]
        if row < 4:
            wall_matrix[row+1][col][1] = not wall_matrix[row+1][col][1]
        if col > 0:
            wall_matrix[row][col-1][1] = not wall_matrix[row][col-1][1]
        if col < 4:
            wall_matrix[row][col+1][1] = not wall_matrix[row][col+1][1]

        return wall_matrix[row][col][0]


    # 1. заполним массив данными
    wall_matrix = []
    for row in range(5):
        row_matrix = []
        for col in range(5):
            if (5*row)+col+1 in on_panels:
                row_matrix.append([(5*row)+col+1, True])
            else:
                row_matrix.append([(5*row)+col+1, False])
        wall_matrix.append(row_matrix)

    for i in wall_matrix: # визуализируем матрицу для удобства дальнейшего планирования
        print(i)


    # 2. Бегаем по матрице сверху вниз и переключаем тумблеры
    # answers = []
    # for row in range(4):
    #     for col in range(5):
    #         if wall_matrix[row][col][1]:
    #             answers.append(switch_light_panel(row+1, col))


    # 3. Делаем тренажер чтобы самостоятельно потыкать и попробовать разные логики решения
    answers = []
    choise = 1
    while 0 < choise < 26:
        choise = int(input("Номер ячейки: "))
        for row in range(5):
            for col in range(5):
                if wall_matrix[row][col][0] == choise:
                    answers.append(switch_light_panel(row, col))


                    for i in wall_matrix:  # визуализируем матрицу для удобства дальнейшего планирования
                        tmp_str = []
                        for j in i:
                            if j[1] == False:
                                if j[0] < 10:
                                    tmp_str.append("0"+str(j[0]))
                                else:
                                    tmp_str.append(str(j[0]))
                            else:
                                if j[0] < 10:
                                    tmp_str.append("*0" + str(j[0]))
                                else:
                                    tmp_str.append("*" + str(j[0]))
                        print(tmp_str)




                    break

    print("\n answers =", answers) # проверяем ответ перед return
    print("\n")
    for i in wall_matrix: # визуализируем матрицу для удобства дальнейшего планирования
        print(i)
    return []




















if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import chain


    def checker(solution, on_panels):
        answer = solution(on_panels)
        wk_p = list((0, 1)[n in on_panels] for n in range(1, 26))
        p = list(wk_p[n: n+5] for n in range(0, 25, 5))
        for a in answer:
            r, c = (a-1) // 5, (a-1) % 5
            p[r][c] = 1 - p[r][c]
            if r+1 < 5:
                p[r+1][c] = 1 - p[r+1][c]
            if r-1 > -1:
                p[r-1][c] = 1 - p[r-1][c]
            if c+1 < len(p[0]):
                p[r][c+1] = 1 - p[r][c+1]
            if c-1 > -1:
                p[r][c-1] = 1 - p[r][c-1]
        return sum(chain(*p)) == 0

    assert checker(wall_keeper, [5, 7, 13, 14, 18]), 'basic'
    assert checker(wall_keeper, list(range(1, 26))), 'all_lights'

