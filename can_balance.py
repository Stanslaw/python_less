from typing import Iterable

def can_balance(weights: Iterable) -> int:
    # your code here

    if len(weights) == 1:
        print("Answer = ", 0)
        return 0

    def find_weights_d(l_data):
        """ Take a list - return a Tuple have balance and point of balance """
        print(l_data)
        position_x = l_data.index("X")
        # print(position_x)
        left = 0
        right = 0

        for idx, val in enumerate(l_data):
            if idx < position_x:
                left += val*(position_x - idx)
            elif idx > position_x:
                right += val*(idx - position_x)

        print(left, right)

        if left == right:
            return(True, position_x)
        else:
            return(False, position_x)


    # Going to all elements and forming differetn center position
    for idx, val in enumerate(weights):
        if 0<idx<len(weights)-1:
            tmp = weights[:]
            tmp[idx] = "X"
            x = find_weights_d(tmp)
            if x[0]:
                print("Answer = ", x[1])
                return x[1]

    print("Answer = ", -1)
    return -1


if __name__ == '__main__':
    # print("Example:")
    # print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")