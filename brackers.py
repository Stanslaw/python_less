def checkio(expression):
    brackers = []
    open_brackers = ["(", "[", "{"]
    close_brackers = [")", "]", "}"]
    alpha_brackers = {"(": ")", "[": "]", "{": "}"}
    for i in expression:
        # print("i -", i)
        if i in open_brackers:
            brackers.append(i)
            # print(brackers)
        if i in close_brackers:
            if not brackers or alpha_brackers[brackers.pop()] != i:
                # print(brackers)
                return False
            
    return True if not brackers else False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((1+(1+1))))]") == False
