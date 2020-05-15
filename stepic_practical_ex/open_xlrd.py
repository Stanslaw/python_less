import xlrd, xlwt

rb = xlrd.open_workbook('salaries.xlsx')

sheet = rb.sheet_by_index(0)

vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

subject = vals[4][:]

# Ищем медианные зарплаты
zp = []
for i in vals[1:]:
    median_element = len(i)//2 + 1
    median = sorted(i[1:])[median_element]
    print(i, median)
    zp.append((i[0], median))

print("_______________")
print(sorted(zp, key=lambda x: x[1], reverse=True)[0][0])

# print(vals[0])

proff = []
for j in range(1, len(vals[0])):
    # print(vals[0][j])
    tmp = []
    for k in range(0, len(vals)):
        tmp.append(vals[k][j])

    proff.append([tmp[0], sum(tmp[1:])/len(tmp[1:])])

print(sorted(proff, key=lambda x: x[1], reverse=True)[0][0])