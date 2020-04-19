def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    if pattern == "*":
        return True

    file_i = 0
    pat_i = 0
    symbols = []
    flag = False

    while file_i < len(filename) and pat_i < len(pattern):

        if pattern[pat_i] == "[":
            while pattern[pat_i] != "]":
                pat_i += 1
                symbols.append(pattern[pat_i])
            symbols.pop()
            # Делаем флаг который возвращает значение подходит ли паттерн под имя или нет в зависимости
            # от восклицательного знака в начале
            if symbols == []:
                flag = False
            elif symbols[0] == "!":
                flag = filename[file_i] not in symbols[1:]
            else:
                flag = filename[file_i] in symbols
            print("Symbols", symbols)


        # Если паттерн не равен * - просто перебираем имя вместе с паттерном посимвольно
        elif pattern[pat_i] != "*":
            # Перебераем одновременно и имя файла и паттерн
            # Если патерн совпадает с именет или имеет знак вопроса - идем дальше
            # Если нет - сразе ваозвращаем False

            if (pattern[pat_i] in [filename[file_i], "?"]) or flag:
                print(pattern[pat_i], filename[file_i])
                file_i += 1
                pat_i += 1
                continue
            else:
                print("False")
                return False
            flag = False

        elif pattern[pat_i] == "*":
            # Если звездочка в паттерне последний символ - значит выводим True
            if pat_i == len(pattern) - 1:
                print("True")
                return True
            # Если следующий за звездочкой символ не равен имени файла движемся дяльше
            else:
                if pattern[pat_i + 1] == "*":
                    pat_i += 1
                    continue
                if pattern[pat_i + 1] != filename[file_i]:
                    file_i += 1
                    continue
                # Когда за звездочной символ совпал - считаем что звездочка отработала и можно перебирать за ней
                else:
                    file_i += 1
                    pat_i += 2
                    continue

            #####

    # Если весь паттерн сработал - значит True, если что-то осталось - нет
    return True if pat_i == len(pattern) else False


if __name__ == '__main__':
    # print("Example:")
    # print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert unix_match('somefile.txt', 'somefile.txt') == True
    # assert unix_match('1name.txt', '[!abc]name.txt') == True
    # assert unix_match('log1.txt', 'log[!0].txt') == True
    # assert unix_match('log1.txt', 'log[1234567890].txt') == True
    # assert unix_match('log1.txt', 'log[!1].txt') == False
    assert unix_match("name.txt", "name[]txt") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
