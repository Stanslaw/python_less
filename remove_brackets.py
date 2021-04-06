def remove_brackets(line: str) -> str:
    # your code here
    print(line)
    brackers_result = []
    open_brackets = {'(':')', '[':']', '{':'}'}
    close_brackets = {')':'(', ']':'[', '}':'{'}

    for idx, val in enumerate(line):
        brackers.append((val, idx))

    print(brackers)

    print(brackers[0][0])

    stack = []
    stack_closet = []

    def compare_first_and_last_brackers (brackers):

        # Рекурсия останавливается когда на вход приходит пустой список
        if not brackers:
            return False
        # Если первая скобка закрывающая, очевидно она мусорная продолжаем без нее
        if brackers[0][0] in close_brackets.keys():
            compare_first_and_last_brackers(brackers[1:])
        # Если последняя скобка открывающая, очевидно она мусорная продолжаем без нее
        if brackers[-1][0] in open_brackets.keys():
            compare_first_and_last_brackers(brackers[:-1])

        # Если дошли до сюда значит по краям скобки правильной направленности, осталось сравнить их по типу.
        # Если обе одинаковые записываем их в стэк как правильную возможную пару.
        if brackers[0][0] == close_brackets[brackers[-1][0]]:
            brackers_result.append([brackers[0][1], brackers[-1][1]])
            compare_first_and_last_brackers(brackers[1:-1])

        # Если разные создаем два инварианта. Удаляем левую и правую и продолжаем рекурсию.

    # print(list(open_brackets.keys()))
    #
    # for idx, i in enumerate(line):
    #     if not stack:
    #         stack.append((i, idx))
    #     elif i in list(open_brackets.keys()):
    #         stack.append((i, idx))
    #     elif i in list(close_brackets.keys()):
    #
    #         if close_brackets[i] == stack[-1]:
    #             stack.pop(-1)
    #
    #     # print(i)
    #
    # print(stack)

    return line


if __name__ == '__main__':
    # print("Example:")
    # print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
