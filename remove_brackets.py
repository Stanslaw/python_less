def remove_brackets(line: str) -> str:
    # your code here
    print(line)
    open_brackets = {'(':')', '[':']', '{':'}'}
    close_brackets = {')':'(', ']':'[', '}':'{'}

    stack = []

    print(list(open_brackets.keys()))

    for idx, i in enumerate(line):
        if not stack:
            stack.append((i, idx))
        elif i in list(open_brackets.keys()):
            stack.append((i, idx))
        elif i in list(close_brackets.keys()):
            pass
        print(i)

    print(stack)

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
