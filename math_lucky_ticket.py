from random import randint
import operator
def checkio(data):

    #replace this for solution

    # сначала,наверное, надо разбить число на все возможные варианты слагаемых

    variants = []
    data_list = []


    def concatinate(sec_f, num_x_f):
        """
        Функция принимает последовательность (пример. ['5', '9', '5', '3', '4', '7']) и возвращает последовательность
        в котокрой слеплены два символа начиная с символа под номером num_x
        """

        output = []
        # print(sec_f)
        # print(num_x_f)
        for idx, val in enumerate(sec_f):
            if idx < num_x_f or idx > num_x_f+1:
                output.append(val)
            elif idx == num_x_f:
                output.append(val + sec_f[idx+1])
        # print("OUT", output)
        return output



    for i in data:
        data_list.append(i)

    variants.append(data_list)
    
    # print(variants)


    # Мы случайным образом будем слеплять два соседних символа и добавлять о общую базу
    # заодно ищем и пропускаем совпадения
    all_iteration = 0
    n = 0
    while len(variants) < 16:
        all_iteration += 1
        n += 1
        for sec in variants:
            all_iteration += 1
            if len(sec) == 1:
                break
            num_x = randint(0, len(sec)-2)
            new_sequence = concatinate(sec, num_x)
            if new_sequence not in variants:
                variants.append(new_sequence)


    print(variants, len(variants), all_iteration)




    # потом подставлять все возможные варианты математических знаков



    return True or False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio('000000') == True, "All zeros"
    # assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('593347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    # assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
