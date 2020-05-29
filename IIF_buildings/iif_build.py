import pandas as pd
import re
from datetime import date, datetime

data = pd.read_excel("C:/Users/Stanslaw/Desktop/table_abon.xlsx")
data2 = data.iloc[1:,[0,1,2,3,4,8]]
data2.columns = data.iloc[0,[0,1,2,3,4,8]]

print(data2)

data_street_serpuhov = {}
data_region = []

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
            # print("IF - ", num1, num2)
        elif not re.findall(r'-|/', num1):
            num2 = str(*re.findall(r'\D+', num1))
            num1 = int(*re.findall(r'\d+', num1))
            # print("ELIF - ", num1, num2)
        else:
            num1, num2 = re.split(r'-|/', num1)
            # print(num1, num2)
            num1 = int(num1)
            # print("ELSE - ", num1, num2)




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

def region_search(name):
    """"
    Принимаем название деревни. Если там нет формальных признаков - пос., дер., с. возвращаем False
    """

    if re.findall(r'дер\.$|пос\.$|с\.$|СНТ|КП|Серпухов-|ДНП|ст\.', name):
        return True
    # print(name)
    return False


# Устанавливаем правила формирования префиксов
correct_prefix = {"бульвар":"Бульвар",
                  "переулок":"пер.",
                  "пер":"пер.",
                  "ул":"ул.",
                  "пр-д":"проезд",
                  "пр-т":"проспект",
                  "пл.":"площадь"
                  }


iter_cust = 0
all_abonents = 0
fresh_date = datetime(2000, 1, 1)
print()

for nas in data2.values[:]:

    # Вычисляем самую свежую дату

    # Последняя синхронизация с БД
    iter_cust += 1
    if isinstance(nas[5], datetime) and fresh_date < nas[5]:
        fresh_date = nas[5]

    # Подсчет всех абонентов
    if isinstance(nas[4], int):
        all_abonents += nas[4]



    # Основной цикл перебора всех адресов и фильтрация многоквартирных домов Серпухова
    if nas[0] == "Серпухов" and street_search(nas[1]):
        # print(nas[0], nas[1], nas[2], sep=" - ")

        # меняем все неправильные префиксы на правильные
        # если есть упоминание без точки - меняем на упоминание с точкой или как в словаре
        if re.findall(r'пер$|ул$|пр-д|пр-т|пл\.|переулок|\bбульвар', nas[1]):
            for i, j in correct_prefix.items():
                # По ходу цикла входные данные могут меняться поэтому еще одна проверка
                if re.findall(r'пер$|ул$|пр-д|пр-т|пл\.|переулок|\bбульвар', nas[1]):
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

    elif nas[0] not in ["Серпухов", "Сепрухов"]:
        # print(nas[0])
        if region_search(nas[0]):
            data_region.append(nas[0])

    elif not street_search(nas[1]) and (nas[1] not in ["дом", "Серпухов", "Сепрухов"]):
        if region_search(nas[1]):
            data_region.append(nas[1])
        # print(nas[0], nas[1])


data_region = sorted(list(set(data_region)))



# Конечный цикл формирования данных по Серпухову
for strt in sorted(data_street_serpuhov):
    # print(strt, end=" - ")
    tmp = []

    for house_num in sorted(data_street_serpuhov[strt]):
        # print(house_num[1], end=", ")
        if house_num[1] != "" and house_num[1] not in tmp:
            # print(house_num[1])
            tmp.append(house_num[1])

    data_street_serpuhov[strt] = tmp




# Записываем в файл данные в виде HTML странички

f = open('abon_html.txt', 'w', encoding="utf-8")
# Формируем первый блок
f.write('''[vc_row][vc_column][vc_column_text]Институт инженерной физики в соответствии с решением Администрации города Серпухова, осуществляет строительство локальной компьютерной сети с выходом в Интернет в семи условно обозначенных районах города Серпухова, а также в Серпуховском районе.[/vc_column_text][/vc_column][/vc_row]''')
# Второй блок, первый столбец - данные по деревням
f.write('''[vc_row][vc_column width="1/2"][vc_column_text]\n''')

for vilage in data_region:
    f.write(f'''    <div class="vilage_button_cust">{vilage}</div>\n''')

f.write('''[/vc_column_text][/vc_column][/vc_row]''')


# Второй блок, второй столбец - данные по Серпухову

f.write('''\n[vc_row][vc_column width="1/2"][vc_column_text]<h2 align="center">Cерпухов</h2>
<table class="matros radius" border="0" width="100%" cellspacing="1" cellpadding="5">
<tbody>
<tr>
    <th align="center" valign="top" width="150">Название улицы</th>
    <th align="center" valign="top">Номер дома</th>
</tr>\n''')


for street, adress in sorted(data_street_serpuhov.items()):
    f.write(f'''<tr>
    <td>{street}</td>
    <td>{", ".join(adress)}</td>
</tr>\n ''')

f.write('''</tbody>
</table>
[/vc_column_text][/vc_column][/vc_row]''')

f.close()



# Здесь выводим всю информацию на экран

# Актуальность данных, последняя синхронизация
print("Последняя синхронизация -", fresh_date, end="\n\n")
# Количество абонентов
print("Общее количество абонентов - ", all_abonents , end="\n\n")
# Количество деревень
print("Количество деревень - ", len(data_region), end="\n\n")
# Количество улиц
print("Количество улиц - ", len(data_street_serpuhov), end="\n\n")
# Деревни и поселки
print(data_region, end="\n\n")
# Адреса Серпухов
print(sorted(data_street_serpuhov.items()), end="\n\n")