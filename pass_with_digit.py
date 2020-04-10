# Taken from mission Acceptable Password I
import re
def is_acceptable_password(password: str) -> bool:
    # your code here

    # если содержит слово Password - False
    if re.findall("password", password.lower()):
        return False

    # если только из цифр
    flag = False
    for i in password:
        if not i.isdigit():
            flag = True
            break

    # если длинна больше 9 можно и одни цифры
    flag2 = False
    if len(password) > 9:
        flag2 = True

    bd_pass = []
    for i in password:
        bd_pass.append(i)

    len_bd_pass = len(set(bd_pass))

    # print(len_bd_pass)

    if len_bd_pass >= 3 and (flag2 or flag and len(password) > 6 and password[-1].isdigit()):
        return True

    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
