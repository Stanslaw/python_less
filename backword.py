def backward_string_by_word(text: str) -> str:
    # your code here
    back_text = ""
    tmp_text = ""
    for i in text:
        if i == " ":
            back_text += tmp_text[::-1]
            # print("!!", back_text)
            tmp_text = ""
            back_text += i
        else:
            tmp_text += i
            # print(tmp_text)

    back_text += tmp_text[::-1]
    print(back_text)
    return back_text


if __name__ == '__main__':
    # print("Example:")
    # print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
