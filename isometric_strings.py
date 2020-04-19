def isometric_strings(str1: str, str2: str) -> bool:
    # your code here
    first = []
    second = []
    shifr = {}

    tmp = []

    for i in str1:
        first.append(i)
    for i in str2:
        second.append(i)
    # Если у строк одинаковая длинна просто бежим посимвольно формируя алфавит
    # затем проверяем работает ли расшифровка
    if len(first) == len(second):
        for i in range(len(first)):
            shifr[first[i]] = second[i]

        for i in range(len(first)):
            tmp.append(shifr[first[i]])

        print("TMP", tmp, "Second", second)
        if tmp == second:
            return True


    return False


if __name__ == '__main__':
    # print("Example:")
    # print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert isometric_strings('add', 'egg') == True
    # assert isometric_strings('foo', 'bar') == False
    # assert isometric_strings('', '') == True
    # assert isometric_strings('all', 'all') == True
    assert isometric_strings("hall", "hoop") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
