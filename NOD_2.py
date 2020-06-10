def greatest_common_divisor(*args):
    if len(args) == 2:
        return gcd(*args)
    print(1)
    return greatest_common_divisor(gcd(*args[:2]), *args[2:])


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
    assert greatest_common_divisor(2226172404, 2652430846, 3702223254, 3260139372, 2021191608) == 2, "Repeating arguments"
    assert greatest_common_divisor(32,256,2048,16384,131072,1048576,8388608,67108864,536870912,4294967296) == 32
