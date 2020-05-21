import zipfile
import os
import xlrd


# with zipfile.ZipFile("rogaikopyta.zip", 'r') as zip_ref:
#     zip_ref.extractall("./unzipped/")

tree = os.walk("unzipped")

all_worker = []

for adress, dir, files in tree:
    print(adress)
    print(files)
    break

for i in files:

    url = adress + "/" + i

    book = xlrd.open_workbook(url)
    sheet = book.sheet_by_index(0)

    rows = [sheet.row_values(row_c) for row_c in range(sheet.nrows)]
    all_worker.append([rows[1][1], rows[1][3]])

print(all_worker)

for i in sorted(all_worker, key=lambda x: x[0]):
    print(i[0], int(i[1]))



