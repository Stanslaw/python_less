def chess_knight(start, moves, results=None):
    if not results:
        results = []

    max_matrix = 7
    matrix_col = "abcdefgh"
    matrix_row = "12345678"

    moves -= 1

    start_col = start[0]
    start_row = start[1]

    for col in [-2, -1, 1, 2]:
        for row in [-2, -1, 1, 2]:
            if abs(col) != abs(row):
                print("col =", col, "row =",  row)

                check_range_col = matrix_col.index(start_col) + col
                check_range_row = matrix_row.index(start_row) + row

                if (0 <= check_range_col <= max_matrix) and (0 <= check_range_row <= max_matrix):
                    new_start_col = matrix_col[check_range_col]
                    new_start_row = matrix_row[check_range_row]
                    new_start = new_start_col + new_start_row

                    print("Moves = ", moves, "New start", new_start, "results =", results)

                    if new_start not in results:
                        results.append(new_start)

                        if moves > 0:
                            print("!!!!!!!!! We go to next step recurcy")
                            results = chess_knight(new_start, moves, results)

    print("Results= ", sorted(results))
    print()
    return sorted(results)

if __name__ == '__main__':
    # print("Example:")
    # print(chess_knight('a1', 1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")
