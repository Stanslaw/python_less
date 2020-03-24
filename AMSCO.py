def decode_amsco(message, key):

    def size_rows(matrix, col):
        """
        Функция принимает матрицу и номер солонки и возвращает количество строк
        """
        row = 0
        while True:
            try:
                matrix[row][col]
                row += 1
            except IndexError:
                # print("row - ", row)
                return row

        return 0

    def strok_gen(lit):
        """
        Функция принимает количество символов и выдает очередную порцию
        """
        if lit == 1:
            return message_mass.pop(0)
        else:
            return message_mass.pop(0)+message_mass.pop(0)


        return 0

    # надо определить сколько у таблицы строк

    len_message = len(message)
    len_key = len(str(key))
    # print("len_message = ", len_message)
    # print("len_key = ", len_key)

    # делаем соотношение столбцов и ключей
    slovar_key = {}
    for idx_c, val in enumerate(str(key)):
        slovar_key[int(val) - 1] = idx_c

    # print(slovar_key)

    # переводим строку в массив чтобы было проще оперировать данными
    message_mass = []
    for i in message:
        message_mass.append(i)

    # Грузим матрицу как есть чтобы понять сколько строк получается и где по одному символу а где по 2 должно быть

    secret_matrix = []
    while len_message > 1:
        if secret_matrix == [] or secret_matrix[-1][0][1] == 2:
            idx = False
        else:
            idx = True
        tmp_secret_matrix = []
        for i in str(key):
            if len_message > 1:
                if not idx:
                    tmp_secret_matrix.append([message_mass.pop(0), 1])
                    len_message -= 1
                    idx = not idx
                else:
                    tmp_secret_matrix.append([message_mass.pop(0) + message_mass.pop(0), 2])
                    len_message -= 2
                    idx = not idx
            # len_message -= 1
        secret_matrix.append(tmp_secret_matrix)

    # Добавляем в матрицу последний элемент 1 или 2 символа, если лист вустой - ничего не добавляем
    if message_mass:
        secret_matrix[-1].append([*message_mass, len(message_mass)])

    # for i in secret_matrix: # мартица правильной размерности
    #     print(i)



    # Переписываем матрицу в связи со сформированными правилами

    # переводим строку в массив чтобы было проще оперировать данными
    message_mass = []
    for i in message:
        message_mass.append(i)
    # print(message_mass)

    for col in range(len_key):
        # нужна функия считающая количество строк в столбце
        for row in range(size_rows(secret_matrix, slovar_key[col])):
            # print("ROW, COL - ", row, slovar_key[col])
            secret_matrix[row][slovar_key[col]][0] = strok_gen(secret_matrix[row][slovar_key[col]][1])

    # for i in secret_matrix:
    #     print(i)



    # Теперь надо вывести сообщение
    message = ""
    for row in range(size_rows(secret_matrix, 0)):
        for col in range(len_key):
            try:
                message += secret_matrix[row][col][0]
            except IndexError:
                print(message)
                return message

    print(message)
    return message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
