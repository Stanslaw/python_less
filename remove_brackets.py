import itertools

def remove_brackets(line: str) -> str:
    # your code here
    print(line)
    brackers = []
    brackers_result = []
    open_brackers = {'(':')', '[':']', '{':'}'}
    close_brackers = {')':'(', ']':'[', '}':'{'}

    for idx, val in enumerate(line):
        brackers.append((val, idx))

    print(brackers)
    print("")

    # print(brackers[0][0])

    def compare_first_and_last_brackers(brackers):

        # Recursion stops when an empty list arrives at the input
        if len(brackers) < 2:
            # print("Exit")
            # print('')
            return True

        # If both are the same at the edges of the brackets, we write them to the stack as the correct possible pair.
        pair_of_brackets = [brackers[0][1], brackers[-1][1]]
        if brackers[0][0] in open_brackers.keys() and brackers[-1][0] in close_brackers.keys() \
                and brackers[0][0] == close_brackers[brackers[-1][0]] \
                and pair_of_brackets not in brackers_result:
            brackers_result.append(pair_of_brackets)
            # compare_first_and_last_brackers(brackers[1:-1])

        # Next, we create two invariants. We delete the left and right and continue the recursion.
        compare_first_and_last_brackers(brackers[1:])
        compare_first_and_last_brackers(brackers[:-1])

        return True

    def brackers_back(data):
        ''' We accept a list with ordinal numbers, return parentheses '''
        back = ''
        dig = []
        # print(data)

        for sym in str(data):
            if sym.isdigit():
                dig.append(int(sym))
        # print(sorted(dig))
        for sym in sorted(dig):
            back += line[sym]
        return back

    def brackers_check(data):
        ''' Accept parentheses, return True or False + number of parentheses '''
        # print('data', data)
        
        # Check the intersection of the parentheses. there must not be two identical digits in the sequence
        for pair in data:
            for el in pair:
                if str(data).count(str(el)) > 1:
                    return (False, None)

        # The brackets must not intersect. Either they stand side by side or inside each other
        if len(data) > 1:
            pairs_of_brackes = list(itertools.permutations(data, 2))
            for a, b in pairs_of_brackes:
                # print("a b", a, b)
                if a[0]<b[0]<a[1] and b[0]<a[1]<b[1]:
                    return (False, None)

        return (True, len(data))




    compare_first_and_last_brackers(brackers)

    # print("FINAL result -", brackers_result, end='\n\n')

    if not brackers_result:
        # If there are no brackets left, the result is obvious.
        return ''

    elif len(brackers_result) == 1:
        # If there is one pair of parentheses, the result is obvious.
        print(brackers_back(brackers_result), end='\n\n')
        return brackers_back(brackers_result)

    # If you need a lot of brackets from the possible, build all valid options
    else:
        combination_breackers = []
        combination_true_breackers = []
        for i in range(1, len(brackers_result)+1):
            # print(i)
            combination_breackers.append(list(itertools.combinations(brackers_result, i)))

        for idx, val in enumerate(combination_breackers[::-1]):
            # print(f"combination {5-idx} -", val, end='\n\n')
            for i in val:
                # print(brackers_check(i))
                valid, len_braker = brackers_check(i)
                # We write only the longest sequences to the final stack
                if (valid and not combination_true_breackers) or (valid and len(combination_true_breackers[-1]) <= len_braker):
                    combination_true_breackers.append(i)
            # print()

        # print('combination_true_breackers -', combination_true_breackers)

    # We are looking for an option with the maximum amount and find it as an answer

    ansver = []
    for variant in combination_true_breackers:
        # print(variant)
        sum = 0
        for i in variant:
            for j in i:
                # print(j)
                sum += j
            if not ansver or ansver['sum']<sum:
                ansver = {'var': variant, 'sum': sum}

    print(brackers_back(ansver['var']), end='\n\n')

    return brackers_back(ansver['var'])


if __name__ == '__main__':
    # print("Example:")
    # print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
