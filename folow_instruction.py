import numpy as np
def follow(instructions):
    # your code here
    instruct = {
        "f": [0, 1],
        "b": [0, -1],
        "l": [-1, 0],
        "r": [1, 0]
    }

    start = np.array([0, 0])

    # nupy library allows you to do itemwise addition

    for i in instructions:
        ins = np.array(instruct[i])
        start = start + ins
    print(tuple(start))
    return tuple(start)


if __name__ == '__main__':
    # print("Example:")
    # print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
