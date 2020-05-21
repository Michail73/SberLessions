import xlrd
import os

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

loc = ("ret2.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

print(listToString(sheet.row_values(2)))


for i in range(2):
    d=open("ed%s.txt" % i, "a+")
    d.write(listToString(sheet.row_values(i))+ '\n')
    d.close()