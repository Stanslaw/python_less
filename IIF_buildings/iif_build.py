import pandas as pd

data = pd.read_excel("table_2020-05-26_15-55.xlsx")
data2 = data.iloc[1:,:4]
data2.columns = data.iloc[0,:4]

data_street_serpuhov = {}
data_region = {}

def clear_num(num1, num2):
    """"
    Функция принимает номер дома и корпус и возвращает все вместе одновременно проверяя данные на валидность
    Если в номере дома написана ерунда - чистит
    """
    flag = True


    # Если в номере дома вместо числа строка - значит там вместо номера пояснения, обычно в которых есть номер дома
    # находим с троке число похожее на номер дома и возвращаем как номер
    if isinstance(num1, str):
        num1 = num1.replace(",", "")
        num1_new = num1.replace(".", "").split()
        # print(num1_new, end=" - ")
        for i in num1_new[::-1]:
            if not i.isalpha():
                num1 = i
                flag = False
                # print(num1)
                break
        if flag:
            num1 = ""

    # Если номера корпуса нет позвращаем только номер дома
    if not num2:
        return num1

    # Если номер дома и номер корпуса в нормальном виде - возвращаем все вместе
    if num1 and num2 in ["а", "б", "в", "г", "д", "е", "-а", "-б", "-в", "-г", "-д", "-е"]:
        if num2.isalpha():
            return str(num1) + "-" + str(num2)
        else:
            return str(num1) + str(num2)

    # Если в номере корпуса ерунда позвращаем только номер дома
    if num1:
        return num1
    else:
        return ""


for nas in data2.values[:]:
    if nas[0] == "Серпухов" and "СНТ" not in nas[1]: #and isinstance(nas[2], int):
        # print(nas[0], nas[1], nas[2], sep=" - ")

        num_building = clear_num(nas[2], nas[3])

        if nas[1] in data_street_serpuhov:
            data_street_serpuhov[nas[1]] += [num_building]
        else:
            data_street_serpuhov[nas[1]] = [num_building]
    # print(nas)



for i in sorted(data_street_serpuhov):
    print(i, data_street_serpuhov[i])


# print(data_street_serpuhov)