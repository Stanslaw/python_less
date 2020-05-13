def checkio(text, word):

    text = text.replace(" ", "")
    matrix_text = []
    tmp = []
    i = 0
    max_len_str = 0
    len_str = 0

    # Создаем матрицу с текстом чтобы было удобно работать с вертикальными конструкциями
    while i < len(text):
        if text[i] != "\n":
            tmp.append(text[i].lower())
            i+=1
            len_str+=1
        elif text[i] == "\n":
            matrix_text.append(tmp)
            tmp = []
            i+=1
            max_len_str = len_str if max_len_str<len_str else max_len_str
            len_str = 0

    matrix_text.append(tmp)

    # Добавляем в короткие строки звездочки чтобы все строки были одной длинны
    print(text)
    for i in matrix_text:
        if len(i)< max_len_str:
            i.extend(["*"]*(max_len_str-len(i)))
        print(i)

    def find_the_word(matrix_text, row, col, word):

        word_list = []
        for i in word:
            word_list.append(i)

        # ищем горизонтально
        i = 0
        while i < len(word):

            if col+i < len(matrix_text[0]) and matrix_text[row][col+i] == word[i] and i == len(word)-1:
                # по условию задачи сткоки считаются с единицы, поэтому +1
                return [row+1, col+1, row+1, col+i+1, True]
            if col+i < len(matrix_text[0]) and matrix_text[row][col+i] == word[i]:
                i += 1
            else:
                break


            # Ищем вертикально
        i = 0
        while i < len(word):

            if row+i < len(matrix_text) and matrix_text[row + i][col] == word[i] and i == len(word) - 1:
                # по условию задачи сткоки считаются с единицы, поэтому +1
                print(word[i], end=" ")
                return [row + 1, col + 1, row + i + 1, col + 1, True]
            if row+i < len(matrix_text) and matrix_text[row + i][col] == word[i]:
                print(word[i], end=" ")
                i += 1
            else:
                break

        return [False]




    # Начинаем перебирать матрицу в поисках первой буквы, далее передаем в функцию которая будет пытаться искать слово

    for row in range(len(matrix_text)):
        for col in range(len(matrix_text[0])):
            if matrix_text[row][col] == word[0]:
                # print(word[0])
                posl = find_the_word(matrix_text, row, col, word)
                print("!!!!", posl)
                if posl[-1]:
                    print(posl[0:-1])
                    return posl[0:-1]

    # print(matrix_text)

    return ["Error"]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]