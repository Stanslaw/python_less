from typing import List, Tuple

import itertools
from math import sqrt


def count_chains(circles: List[Tuple[int, int, int]]) -> int:

    # your code here
    print("!!!", circles, "\n")

    chains = []

    # We form a list of all possible combinations
    for ones in itertools.combinations(circles, 2):

        # Rr - distance between centers of circles
        # R - radius of the larger circle
        # r - smaller circle radius

        Rr = sqrt((ones[0][0]-ones[1][0])**2 + (ones[0][1]-ones[1][1])**2)
        R = max([ones[0][2], ones[1][2]])
        r = min([ones[0][2], ones[1][2]])

        # If the square of the sum of the radii is greater than the squares of the legs (according to Pythagoras),
        # the links intersect or are included in each other
        if R - Rr >= r:
            continue
        elif R + r > Rr:
            chains.append([*ones])

    # Now we need to merge the intersecting chains

    for i in range(2**len(circles)):
        if not chains:
            break

        # print("chains = ", chains)
        f_el = chains.pop(0)
        # print("f_el = ", f_el, "\n")

        flag = True

        for chain in chains:

            for i in f_el:
                if i in chain:
                    chain.extend(f_el)
                    flag = False
                    break

        if flag:
            chains.append(f_el)

    # Adding single links to the sequence list
    for cir in circles:
        # print("cir = ", cir)

        if not chains:
            chains.append([cir])

        flag = True

        for i in chains:
            # print("i = ", i, "cir = ", cir)
            if cir in i:
                flag = False
        if flag:
            chains.append([cir])

    print("\n", "chains = ", chains, "len = ", len(chains))
    return len(chains)


if __name__ == '__main__':
    # print("Example:")
    # print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    # assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    # assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    # assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    # assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    # assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    assert count_chains([[1, 3, 1], [2, 2, 1], [4, 2, 1], [5, 3, 1], [3, 3, 1]]) == 1, 'Olymp'
    print("Coding complete? Click 'Check' to earn cool rewards!")
