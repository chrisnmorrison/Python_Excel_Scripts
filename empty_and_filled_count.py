import xlrd

empty = 0
filled = 0
total = 0
path = "my_spreadsheet.xls"
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)
for row in range(sheet.nrows):
    for column in range(sheet.ncols):
        if sheet.cell_value(row, column) == "":
            empty += 1
            total += 1
        else:
            filled += 1
            total += 1
print(f'Empty cells: {empty}.')
print(f'Filled cells: {filled}.')
print(f'Total cells: {total}.')