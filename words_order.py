def words_order(text: str, words: list) -> bool:
    # your code here

    #Walk for splitting text
    for i in text.split():
        #If WORD list have dublicate - return False. It is a strange condition of a task
        if words and words.count(words[0]) > 1:
            return False
        #If first WORD == word of text we delete first WORD and go next
        if words and i == words[0]:
            words.pop(0)
            # print(words)
    #When cicle is over end "words" is EMPTY - retern True
    return False if words else True


if __name__ == '__main__':
    # print("Example:")
    # print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    assert words_order("hi world world im here", ["world", "world"]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
