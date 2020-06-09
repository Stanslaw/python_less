def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """

    def mnoj_nod(x):
        """ Отправляем число - возвращаем список делителей"""
        results = []

        while x>1:
            # print(x)
            for i in range(2, x+1):
                if x%i == 0:
                    x = int(x/i)
                    results.append(i)
                    # print(i)
                    break
        # print(results)
        return results

    data = args
    min_data = min(data)
    nod = []

    print(data, min_data)

    for i in data:
        nod.append(mnoj_nod(i))

    print(nod)

    while [] not in nod:
        flag = True
        for i in nod:
            tmp = i.pop(0)

    # for i in range(min_data+1, 1, -1):
    #     # print(i)
    #     if min_data%i == 0:
    #         flag = True
    #         for j in data:
    #             if j%i != 0:
    #                 flag = False
    #                 break
    #         if flag:
    #             print(i)
    #             return i
    #
    #
    # print(1)
    return 1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert greatest_common_divisor(6, 4) == 2, "Simple"
    # assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    # assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    # assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
    assert greatest_common_divisor(2226172404, 2652430846, 3702223254, 3260139372, 2021191608) == 3, "Repeating arguments"
