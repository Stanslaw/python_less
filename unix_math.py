import re
def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    if pattern == "*":
        return True

    # Проверяем два раза. Слева направо и справа налево
    # если оба теста показывают flag True - позвращаем True
    flag_1 = flag_2 = False
    for i in range(min(len(filename), len(pattern))):
        if pattern[i] == "*":
            print("flag_1 = True")
            flag_1 = True
            break
        if filename[i] == pattern[i] or pattern[i] == "?":
            print(filename[i], "ok")
        else:
            print("False")
            return False
    flag_1 = True


    for i in range(min(len(filename), len(pattern))-1, -1, -1):
        # print("rev = ", i)
        if pattern[i] == "*":
            print("flag_2 = True")
            flag_2 = True
            break
        if filename[i] == pattern[i] or pattern[i] == "?":
            print(filename[i], "ok")
        else:
            print("False")
            return False
    flag_2 = True


    return flag_1*flag_2


if __name__ == '__main__':
    # print("Example:")
    # print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
