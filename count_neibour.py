def count_neighbours(grid, row, col):

    max_matrix_row = len(grid)
    max_matrix_col = len(grid[0])

    print(max_matrix_row, max_matrix_col)

    neighour = 0

    for i_row in range(-1, 2):
        for j_col in range(-1, 2):
            if (0 <= (row+i_row) < max_matrix_row) and (0 <= (col+j_col) < max_matrix_col) and not (i_row == j_col == 0):
                neighour += grid[row+i_row][col+j_col]

    print(neighour)
    return neighour


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
