import numpy as np
import xlrd

rb = xlrd.open_workbook('trekking2.xlsx')

sheet1 = rb.sheet_by_index(0)
sheet2 = rb.sheet_by_name("Раскладка")

KBJU = list(zip(sheet1.col_values(0, 1), sheet1.col_values(1, 1), sheet1.col_values(2, 1), sheet1.col_values(3, 1),
                sheet1.col_values(4, 1)))
KBJU2 = {}

for val in KBJU:
    tmp = list(val[1:])
    # print(tmp)
    for idx, val1 in enumerate(tmp):
        if not val1:
            # print("Have none")
            tmp[idx] = 0
        # print(tmp)
    KBJU2[val[0]] = tmp

gramms = list(zip(sheet2.col_values(0, 1), sheet2.col_values(1, 1)))

print(gramms)

summ_cust = np.array([0., 0., 0., 0.])

for i in gramms:
    tmp = np.array(KBJU2[i[0]]) * i[1] / 100
    summ_cust += tmp
    # print(tmp)


print(KBJU2)
# print(gramms2)
print(summ_cust)



