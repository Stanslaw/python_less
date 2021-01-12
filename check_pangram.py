def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    text = text.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_list = [x for x in alpha]
    # print(alpha_list)

    for i in text:
        if i in alpha_list:
            alpha_list.remove(i)

    print(alpha_list)

    return True if not alpha_list else False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
