def remove_brackets(line: str) -> str:
    # your code here
    print(line)
    brackers = []
    brackers_result = []
    open_brackers = {'(':')', '[':']', '{':'}'}
    close_brackers = {')':'(', ']':'[', '}':'{'}

    for idx, val in enumerate(line):
        brackers.append((val, idx))

    print(brackers)
    print("")

    # print(brackers[0][0])

    def compare_first_and_last_brackers(brackers):
        # print('brackers', brackers)
        # print("RECURSY", brackers_result)
        # print("LEN", len(brackers))
        # print('')

        # Рекурсия останавливается когда на вход приходит пустой список
        if len(brackers) < 2:
            # print("Exit")
            # print('')
            return True

        # Если по краям скобки обе одинаковые записываем их в стэк как правильную возможную пару.
        pair_of_brackets = [brackers[0][1], brackers[-1][1]]
        if brackers[0][0] in open_brackers.keys() and brackers[-1][0] in close_brackers.keys() \
                and brackers[0][0] == close_brackers[brackers[-1][0]] \
                and pair_of_brackets not in brackers_result:
            brackers_result.append(pair_of_brackets)
            # compare_first_and_last_brackers(brackers[1:-1])

        # Далее создаем два инварианта. Удаляем левую и правую и продолжаем рекурсию.
        compare_first_and_last_brackers(brackers[1:])
        compare_first_and_last_brackers(brackers[:-1])

        return True

    compare_first_and_last_brackers(brackers)

    print("FINAL result -", brackers_result)


    # Теперь из возможных скобок надо построить все валидные варианты


    return line


if __name__ == '__main__':
    # print("Example:")
    # print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    # assert remove_brackets('[][[[') == '[]'
    # assert remove_brackets('[[(}]]') == '[[]]'
    # assert remove_brackets('[[{}()]]') == '[[{}()]]'
    # assert remove_brackets('[[[[[[') == ''
    # assert remove_brackets('[[[[}') == ''
    # assert remove_brackets('') == ''
    # assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
