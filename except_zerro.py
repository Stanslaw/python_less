from typing import Iterable


def except_zero(items: list) -> Iterable:
    # your code here

    zeros = []
    ex_zeros = []

    for idx, val in enumerate(items):
        if val == 0:
           zeros.append(idx)
        else:
            ex_zeros.append(val)

    ex_zeros = sorted(ex_zeros)

    # print("zeros = ", zeros)

    res = []
    n = 0
    while ex_zeros or zeros:
        if zeros == []:
            res.append(ex_zeros.pop(0))
        elif zeros[0] == n:
            res.append(0)
            zeros.pop(0)
        else:
            res.append(ex_zeros.pop(0))
        n += 1

    print(res)
    return res


if __name__ == '__main__':
    # print("Example:")
    # print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")
