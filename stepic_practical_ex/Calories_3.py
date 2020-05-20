import numpy as np
import xlrd

rb = xlrd.open_workbook('trekking3.xlsx')

sheet1 = rb.sheet_by_index(0)
sheet2 = rb.sheet_by_name("Раскладка")

KBJU = list(zip(sheet1.col_values(0, 1), sheet1.col_values(1, 1), sheet1.col_values(2, 1), sheet1.col_values(3, 1),
                sheet1.col_values(4, 1)))
KBJU2 = {}

for val in KBJU:
    tmp = list(map(lambda x: x if x else 0, list(val[1:])))

    # print(tmp)
    # for idx, val1 in enumerate(tmp):
    #     if not val1:
            # print("Have none")
            # tmp[idx] = 0
        # print(tmp)
    KBJU2[val[0]] = tmp

print(KBJU2)

gramms = list(zip(sheet2.col_values(0, 1), sheet2.col_values(1, 1), sheet2.col_values(2, 1)))
print("__________________")
# print(gramms)

all_sums = []
summ_cust = np.array([0., 0., 0., 0.])

day = gramms[0][0]

for i in gramms:
    if day != i[0]:
        # print(summ_cust)
        all_sums.append(list(summ_cust))
        summ_cust = np.array([0., 0., 0., 0.])
        day = i[0]

    tmp = np.array(KBJU2[i[1]]) * i[2] / 100
    summ_cust += tmp
    # print(tmp)

all_sums.append(list(summ_cust))

# print(summ_cust)
for row in all_sums:
    print(*list(map(lambda x: int(x), row)))


