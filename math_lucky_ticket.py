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

    def doing_operation(tmp_var_f, num_position_f, num_operation_f):
        """
        Функция принимаем последовательность, позицию начиная с которой будем производить операцию и номер операции
        (+, -, *, /) и возвращает последовательность в которой совершена операция над соседними элементами
        """

        new_tmp_var = []

        for idx, val in enumerate(tmp_var_f):
            if idx < num_position_f or idx > num_position_f + 1:
                new_tmp_var.append(val)
            elif idx == num_position_f:
                if num_operation_f == 0:
                    new_tmp_var.append(operator.add(float(val),  float(tmp_var_f[idx + 1])))
                elif num_operation_f == 1:
                    new_tmp_var.append(operator.sub(float(val),  float(tmp_var_f[idx + 1])))
                elif num_operation_f == 2:
                    new_tmp_var.append(operator.mul(float(val),  float(tmp_var_f[idx + 1])))
                # elif num_operation_f == 3:
                #     new_tmp_var.append(operator.div(float(val),  float(tmp_var_f[idx + 1])))


        return new_tmp_var


    def try_give_100(var):
        """
        Функция принимает последовательность (пример ['5', '9', '3', '3', '4', '7']) и пытается много раз
        случайным образом совершать математические операции над разными соседними элементами
        последовательности. Если результат равен 100 - выдаем TRUE. Если после 100 итераций сотня так и не набирается
        - False
        """
        exit_idx = 0
        while exit_idx < 100:
            tmp_var = var[:]
            exit_idx += 1

            for _ in range(len(tmp_var)-1):
                if len(tmp_var) == 1:
                    if tmp_var == 100:
                        return True
                    break
                num_position = randint(0, len(tmp_var)-2)
                num_operation = randint(0, 3) # случайным образом выбираем операцию которую будем производить над символами

                tmp_var = doing_operation(tmp_var, num_position, num_operation)

        return False

    for i in variants:
        # print(list(map(lambda x: int(x), i)))
        # отправляем последовательность в функцию т возвращаем True если знаками можно набрать 100
        if try_give_100(list(map(lambda x: int(x), i))):
            return False
        # print(i)



    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio('000000') == True, "All zeros"
    # assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('593347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    # assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
