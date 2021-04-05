from typing import List


def letter_queue(commands: List[str]) -> str:
    # your code here
    # print(commands)

    stack = []

    for command in commands:
        if stack and command == "POP":
            stack.pop(0)
        elif not stack and command == "POP":
            continue
        else:
            com, lit = command.split()
            stack.append(lit)

        # print(com, " - ", lit )

    # print("".join(stack))

    return "".join(stack)


if __name__ == '__main__':
    # print("Example:")
    # print(letter_queue(['PUSH A',
    #     'POP',
    #     'POP',
    #     'PUSH Z',
    #     'PUSH D',
    #     'PUSH O',
    #     'POP',
    #     'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")