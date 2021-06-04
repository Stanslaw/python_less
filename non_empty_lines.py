import re
def non_empty_lines(text: str) -> int:
    # your code here

    not_empty_strings = 0
    for idx, val in enumerate(text.split('\n')):
        string_have_an_any_symbol = re.findall(r'\S', val)
        # print(idx, val, bool(string_have_an_any_symbol))
        if bool(string_have_an_any_symbol):
            not_empty_strings += 1

    return not_empty_strings


if __name__ == '__main__':
    # print("Example:")
    # print(non_empty_lines('one simple line\n'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")