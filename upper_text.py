def is_all_upper(text: str) -> bool:
    # your code here
    if text == "":
        return False

    flag = False
    for i in text:
        if i.isdigit() or i == " ":
            continue
        elif i.isalpha() and i == i.upper():
            flag = True
            continue
        elif i.isalpha() and i == i.lower():
            return False

    if not flag:
        return False
    return True


if __name__ == '__main__':
    # print("Example:")
    # print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
