import operator
def checkio(data):

    #replace this for solution

    # сначала,наверное, надо разбить число на все возможные варианты слагаемых

    variants = []

    def rec_razer(num_tick):

        if len(num_tick) > 1:
            variants.append([num_tick[0:-1], num_tick[-1]] + (variants[-1][1:] if variants else ["none"]))
            rec_razer(num_tick[0:-1])
            # print("+")

        return num_tick


    rec_razer(data)

    print(variants)


    # потом подставлять все возможные варианты математических знаков



    return True or False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio('000000') == True, "All zeros"
    # assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    # assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
