def split_pairs(a):
    # your code here
    result = []
    while len(a) >= 2:
        result.append(a[0] + a[1])
        a = a[2:]
        # print(result)
    if a:
        result.append(a+"_")
    print(result)
    return result


if __name__ == '__main__':
    # print("Example:")
    # print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
