def can_pass(matrix, first, second):

    # 1. Если first != second - сразу нет

    f0, f1 = first
    s0, s1 = second
    genesis_matrix = matrix[f0][f1]
    if matrix[f0][f1] != matrix[s0][s1]:
        return False

    # print(matrix[f0][f1])
    for i in matrix:
        print(i)
    print(first)
    print(second)

    # 2. Методом перебора всех вершин графа начинаем двигаться от старта в поисках вершины финальной.
    # Как только до нее дотягиваемся - выводим True. Нет - нет.

    matrix_max_row = len(matrix)
    matrix_max_col = len(matrix[0])

    # print(matrix_max_col, matrix_max_row)

    def dfs(matrix, start, stop, flag=None, included_vertex=set()):
        if flag == None:
            flag = False

        # Добавляем вершину в которой находимся в посещенные
        included_vertex.add(start)
        print("included_vertex -", included_vertex)

        # Если мы пришли в точку стопа переключаем flag
        if start == stop:
            flag = True
            print("BINGO -", start)
            return [flag, included_vertex]

        # Начинаем перебирать 4 стороны от стартовой точки в поиске гинезиса.
        # Если есть перезапускаем рекурсивную функцию с новой вершиной


        if start[0]>0 and (matrix[start[0]-1][start[1]] == genesis_matrix) and ((start[0]-1, start[1]) not in included_vertex): # вверх от стартовой точки
            new_step = (start[0]-1, start[1])
            flag, included_vertex = dfs(matrix, new_step, stop, flag, included_vertex)

        if start[0]<matrix_max_row-1 and (matrix[start[0]+1][start[1]] == genesis_matrix) and ((start[0]+1, start[1]) not in included_vertex): # вниз от стартовой точки
            new_step = (start[0]+1, start[1])
            flag, included_vertex = dfs(matrix, new_step, stop, flag, included_vertex)

        if start[1]>0 and (matrix[start[0]][start[1]-1] == genesis_matrix) and ((start[0], start[1]-1) not in included_vertex): # влево от стартовой точки
            new_step = (start[0], start[1]-1)
            flag, included_vertex = dfs(matrix, new_step, stop, flag, included_vertex)

        if start[1]<matrix_max_col-1 and (matrix[start[0]][start[1]+1] == genesis_matrix) and ((start[0], start[1]+1) not in included_vertex): # справа от стартовой точки
            new_step = (start[0], start[1]+1)
            flag, included_vertex = dfs(matrix, new_step, stop, flag, included_vertex)


        return [flag, included_vertex]


    end = dfs(matrix, first, second)
    print(end)
    return end[0]


if __name__ == '__main__':
    # assert can_pass(((0, 0, 0, 0, 0, 0),
    #                  (0, 2, 2, 2, 3, 2),
    #                  (0, 2, 0, 0, 0, 2),
    #                  (0, 2, 0, 2, 0, 2),
    #                  (0, 2, 2, 2, 0, 2),
    #                  (0, 0, 0, 0, 0, 2),
    #                  (2, 2, 2, 2, 2, 2),),
    #                 (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
