def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    if pattern == "*":
        return True

    file_i = 0
    pat_i = 0

    while file_i < len(filename) and pat_i < len(pattern):
        # Если паттерн не равен * - просто перебираем имя вместе с паттерном посимвольно
        if pattern[pat_i] != "*":
            # Перебераем одновременно и имя файла и паттерн
            # Если патерн совпадает с именет или имеет знак вопроса - идем дальше
            # Если нет - сразе ваозвращаем False
            if pattern[pat_i] in [filename[file_i], "?"]:
                print(pattern[pat_i], filename[file_i])
                file_i += 1
                pat_i += 1
                continue
            else:
                print("False")
                return False

        else:
            # Если звездочка в паттерне последний символ - значит выводим True
            if pat_i == len(pattern)-1:
                print("True")
                return True
            # Если следующий за звездочкой символ не равен имени файла движемся дяльше
            else:
                if pattern[pat_i+1] == "*":
                    pat_i += 1
                    continue
                if pattern[pat_i+1] != filename[file_i]:
                    file_i += 1
                    continue
                # Когда за звездочной символ совпал - считаем что звездочка отработала и можно перебирать за ней
                else:
                    file_i += 1
                    pat_i += 2
                    continue


    # Если весь паттерн сработал - значит True, если что-то осталось - нет
    return True if pat_i == len(pattern) else False


if __name__ == '__main__':
    # print("Example:")
    # print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert unix_match('somefile.txt', '*') == True
    # assert unix_match('other.exe', '*') == True
    # assert unix_match('my.exe', '*.txt') == False
    # assert unix_match('log1.txt', 'log?.txt') == True
    # assert unix_match('log12.txt', 'log?.txt') == False
    # assert unix_match('log12.txt', 'log??.txt') == True
    # assert unix_match("file19.txt", "*z*") == False
    assert unix_match("log12.txt", "**") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
