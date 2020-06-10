def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """

    def mnoj_nod(x):
        """ Send a digit - return a list of dividers"""
        results = []

        while x>1:
            for i in range(2, x+1):
                if x%i == 0:
                    x = int(x/i)
                    results.append(i)
                    # print(i)
                    break
        return results


    data = args
    nod = []

    print(data)


    # Take an all dividers of all digits - nod
    for i in data:
        nod.append(mnoj_nod(i))

    print(nod)

    final_muls = 1

    # Find dividers who in of all group

    for element in nod[0]:
        flag = True
        for muls in nod[1:]:
            if element in muls:
                muls.remove(element)
                continue
            else:
                flag = False

        # if the digit is in all samples multiplies it in final var
        if flag:
            final_muls *= element

            print(final_muls)

    return final_muls


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
    assert greatest_common_divisor(2226172404, 2652430846, 3702223254, 3260139372, 2021191608) == 2, "Repeating arguments"
    assert greatest_common_divisor(32,256,2048,16384,131072,1048576,8388608,67108864,536870912,4294967296) == 32
