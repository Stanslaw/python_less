def how_deep(structure):
    # your code here
    text_structure = str(structure)
    n = 0
    max_n = 0
    for i in text_structure:
        if i in ['(', '[']:
            n += 1
        elif i in [')', ']']:
            n -= 1

        if max_n < n:
            max_n = n
    print(structure)
    print(max_n)
    return max_n


if __name__ == '__main__':
    # print("Example:")
    # print(how_deep((1, 2, 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
