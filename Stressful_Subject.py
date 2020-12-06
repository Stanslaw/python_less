import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    red_words = ["help", "asap", "urgent"]


    print(subj.upper())

    for i in red_words_re:
        if re.search(i, subj.upper()):
            print("+1", re.search(i, subj.upper()))
            return True

    if subj == subj.upper():
        print("+2")
        return True


    if re.search(r'!!!$', subj):
        print("+3")
        return True

    return False

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    # assert is_stressful("Hi") == False, "First"
    # assert is_stressful("I neeed HELP") == True, "Second"
    # assert is_stressful("asasap help HeLp H!E!L!P! H-E-L-P, even in a very loooong way HHHEEEEEEEEELLP. HIELP") == True, "Second"
    assert is_stressful("Headlamp, wastepaper bin and supermagnificently") == False, "First"

    print('Done! Go Check it!')
