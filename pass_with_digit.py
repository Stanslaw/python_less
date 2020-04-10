# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    # your code here
    flag = False
    for i in password:
        if not i.isdigit():
            flag = True
    if flag and len(password)>6 and password[-1].isdigit():
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
