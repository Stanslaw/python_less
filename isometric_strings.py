def isometric_strings(str1: str, str2: str) -> bool:
    # your code here
    shifr = {}
    tmp = []

    # Если у строк одинаковая длинна просто бежим посимвольно формируя алфавит
    # затем проверяем работает ли расшифровка
    if len(str1) == len(str2):
        for i in range(len(str1)):
            shifr[str1[i]] = str2[i]

        for i in range(len(str1)):
            tmp.append(shifr[str1[i]])

        print("TMP", ''.join(tmp), "str2", str2)
        if ''.join(tmp) == str2:
            return True


    return False


if __name__ == '__main__':
    # print("Example:")
    # print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    assert isometric_strings("hall", "hoop") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
