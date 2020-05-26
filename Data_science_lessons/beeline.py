import pandas as pd
import datetime

bee_data = pd.read_excel("beeline_2.xlsx")

# print(bee_data.head(), "\n\n")

# print(bee_data.keys(), "\n\n")

internet = bee_data[["Дата/Время", "Объем услуг"]]

# print(bee_data[["Сервис", "Объем услуг"]])

call = bee_data[["Дата/Время", "Сервис", "Объем услуг"]]

# print(internet)
sum_mb = 0
cooling_time = datetime.timedelta()
# print(cooling_time)

# print(internet[internet["Объем услуг"].isin(["20 Мбайт"])])

for i in internet.values:
    # print(i[1])
    if "Мбайт" in i[1]:
        sum_mb += float(i[1].split()[0].replace(",", "."))
        print(i[0], " - ", i[1])


print("\nМегабайт в месяц = ", round(sum_mb / 3, 2), "Мб","\n\n" )

for i in call.values:
    if "Исходящий звонок" in i[1]:
        tmp = i[2].split()
        if len(tmp) == 2:
            delta = datetime.timedelta(seconds=int(tmp[0]))
        elif len(tmp) == 4:
            delta = datetime.timedelta(minutes=int(tmp[0]), seconds=int(tmp[2]))
        elif len(tmp) == 6:
            delta = datetime.timedelta(hours=int(tmp[0]), minutes=int(tmp[2]), seconds=int(tmp[4]))
        print(i[0], " - ", delta)
        cooling_time += delta

print("\nOUT calling time in month = ", cooling_time / 3)