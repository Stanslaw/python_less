from itertools import combinations, permutations
def checkio(data):

    #replace this for solution

    combi = []  # all combinations
    for i in range(1, len(data)):
        combi += list(combinations(data, i))

    all_sum = sum(data)  # sum weight of cargo
    min_disbalance = all_sum # min disbalance started from max weight
    for k_comby in combi:
        tmp = abs(sum(k_comby)*2 - all_sum) # disbalance = abs(right_hand - left_hand)
                                            # left_hand = all_sum - right_hand
                                            # finaly
                                            # disbalance = abs(right_hand - (all_sum - right_hand) = abs(right_hand * 2 - all_sum)

        min_disbalance = tmp if min_disbalance > tmp else min_disbalance

    # print(combi)
    # print(all_sum)
    # print(min_disbalance)

    return min_disbalance


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
