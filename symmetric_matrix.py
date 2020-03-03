def checkio(matrix):


    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != (-1 * matrix[col][row]):
                print("False")
                return False

    print("True")
    return True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # print("Example:")
    # print(checkio([
    #     [0, 1, 2],
    #     [-1, 0, 1],
    #     [-2, -1, 0]]))

    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!");
