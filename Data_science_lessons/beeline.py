import pandas as pd
import datetime

bee_data = pd.read_excel("beeline.xlsx")

# print(bee_data.head(), "\n\n")

# print(bee_data.keys(), "\n\n")

internet = bee_data[["Дата/Время", "Объем услуг"]]

# print(bee_data[["Сервис", "Объем услуг"]])

call = bee_data[["Дата/Время", "Сервис", "Объем услуг"]]

# print(internet)
sum_mb = 0
cooling_time = datetime.timedelta()
# print(cooling_time)

for i in internet.values:
    # print(i[1])
    if "Мбайт" in i[1]:
        sum_mb += float(i[1].split()[0].replace(",", "."))
        print(i[0], " - ", i[1])


print("Мегабайт в месяц = ", sum_mb, "Мб","\n\n" )

for i in call.values:
    if "Исходящий звонок" in i[1]:
        print(i[0], end=" - ")
        tmp = i[2].split()
        if len(tmp) == 2:
            delta = datetime.timedelta(seconds=int(tmp[0]))
        elif len(tmp) == 4:
            delta = datetime.timedelta(minutes=int(tmp[0]), seconds=int(tmp[2]))
        print(delta)
        cooling_time = cooling_time + delta

print("\n OUT calling time in month = ", cooling_time)