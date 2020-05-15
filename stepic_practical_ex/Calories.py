import xlrd

rb = xlrd.open_workbook('trekking1.xlsx')

sheet = rb.sheet_by_index(0)

vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

products = []
for i in vals[1:]:
    products.append(i[:2])
    # print(i)
products = sorted(products, key=lambda x: (-x[1], x[0]))
for i in products:
    print(i[0])