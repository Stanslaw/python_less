def decode_amsco(message, key):

    # надо определить сколько у таблицы строк

    len_message = len(message)
    len_key = len(str(key))
    print("len_message = ", len_message)
    print("len_key = ", len_key)

    # делаем соотношение столбцов и ключей
    slovar_key = {}
    for idx_c, val in enumerate(str(key)):
        slovar_key[int(val)] = idx_c

    print(slovar_key)

    message_mass = []
    for i in message:
        message_mass.append(i)

    # Грузим матрицу как есть чтобы понять сколько строк получается и где по одному символу а где по 2 должно быть
    idx = True
    secret_matrix = []
    while len_message > 1:
        idx = not idx
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

    for i in secret_matrix:
        print(i)



    # Переписываем матрицу в связи со сформированными правилами


    return message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    # assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    # assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
