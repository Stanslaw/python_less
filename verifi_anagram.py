def verify_anagrams(first_word, second_word):

    def convert_word(word):
        list_word = []
        for i in word:
            if i != " ":
                list_word.append(i.lower())
        print(sorted(list_word))
        return sorted(list_word)

    return convert_word(first_word) == convert_word(second_word)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

