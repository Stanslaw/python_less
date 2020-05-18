def goes_after(word: str, first: str, second: str) -> bool:
    # your code here

    flag = False

    for i in word:
        # print(i, flag)
        if flag:
            return True if i == second else False

        if i in [first, second] and i == second:
            # print("False")
            return False
        elif i in [first, second]:
            flag = True

    return False

if __name__ == '__main__':
    # print("Example:")
    # print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    assert goes_after("almaz","m","a") == False

    print("Coding complete? Click 'Check' to earn cool rewards!")
