import pandas as pd
import re

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
            num1 = 0

        # Здесь надо из num1 изьять префик который пойдет в num2
        if isinstance(num1, int) or num1.isdigit():
            num1 = int(num1)
        else:
            print(num1)
            num1, num2 = re.split(r'-|/', num1)
            # print(num1, num2)
            num1 = int(num1)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





    # Если номера корпуса нет позвращаем только номер дома
    if not num2:
        return (num1, str(num1))

    # Если номер дома и номер корпуса в нормальном виде - возвращаем все вместе
    if num1 and num2 in ["а", "б", "в", "г", "д", "е", "-а", "-б", "-в", "-г", "-д", "-е"]:
        if num2.isalpha():
            return (num1, str(num1) + "-" + str(num2))
        else:
            return (num1, str(num1) + str(num2))

    # Если в номере корпуса ерунда позвращаем только номер дома
    if num1:
        return (num1, str(num1))
    else:
        return (0, "")


def street_search(street):
    """
    Принимаем название улицы и проверяем чтобы это была именно улица, без префиксов СНТ, дер. и т.д
    Если префикс есть - возвращаем False и не включаем строку в перебор
    """

    answer = re.findall(r'СНТ|дер\.|\bдом|ст\.|ДНП', street)

    # if bool(answer):
    #     print(street, answer)

    return not bool(answer)


# Устанавливаем правила формирования префиксов
correct_prefix = {"переулок":"пер.",
                  "пер":"пер.",
                  "ул":"ул.",
                  "пр-д":"проезд",
                  "пр-т":"проспект",
                  "пл.":"площадь"
                  }



for nas in data2.values[:]:

    # Основной цикл перебора всех адресов и фильтрация многоквартирных домов Серпухова
    if nas[0] == "Серпухов" and street_search(nas[1]):
        # print(nas[0], nas[1], nas[2], sep=" - ")

        # меняем все неправильные префиксы на правильные
        # если есть упоминание без точки - меняем на упоминание с точкой или как в словаре
        if re.findall(r'пер$|ул$|пр-д|пр-т|пл\.|переулок', nas[1]):
            for i, j in correct_prefix.items():
                # По ходу цикла входные данные могут меняться поэтому еще одна проверка
                if re.findall(r'пер$|ул$|пр-д|пр-т|пл\.|переулок', nas[1]):
                    nas[1] = nas[1].replace(i, j)

        # делаем проверку адресов, если в тексте нет ул. пер. и тд. подставляем в конец УЛ.
        # потому что переодически встречаются адреса без префикса
        if not re.findall(r'\bул|\bпер|\bпроезд|\bшоссе|\bпл|\bпр\-д|\bбульвар|\bмкр|\bпр\-т', nas[1]):
            nas[1] += " ул."
            # print(nas[1])

        num_building = clear_num(nas[2], nas[3])

        if nas[1] in data_street_serpuhov:
            data_street_serpuhov[nas[1]] += [num_building]
        else:
            data_street_serpuhov[nas[1]] = [num_building]
    # print(nas)



for strt in sorted(data_street_serpuhov):
    print(strt, end=" - ")
    for house_num in data_street_serpuhov[strt]:
        print(house_num, end=", ")

    print()


# print(data_street_serpuhov)