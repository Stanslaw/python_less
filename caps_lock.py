def caps_lock(text: str) -> str:
    # your code here
    caps_check = False
    result = ""
    print(text)

    for i in text:
        if i == i.upper():
            result += i
            continue

        if i in ["a", "A"]:
            caps_check = not caps_check
            # print(caps_check)
            continue


        if not caps_check:
            result += i
        elif caps_check:
            if i == i.upper():
                result += i.lower()
            else:
                result += i.upper()

        # print(i)

    print(result)
    return result


if __name__ == '__main__':
    # print("Example:")
    # print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Madder than Mad Brian of Madcastle") == "MDDER THn MD BRIn of MDCstle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
