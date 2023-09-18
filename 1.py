import datetime
import timeit
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet("Sheet 1")

def F1(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return (F1(n-1)+F1(n-2))

def F2(n, dic = {0: 0, 1: 1}):
    if n not in dic:
        dic[n] = F2(n-1, dic) + F2(n-2, dic)
    return dic[n]

measure1 = {0:0,1:0}
measure2 = {0:0,1:0}

for i in range(2,35+1):
    st = datetime.datetime.now()
    F1(i)
    ed = datetime.datetime.now()
    elapsed = ed-st
    measure1[i] = elapsed.total_seconds()
    sheet1.write(i,0,i)
    sheet1.write(i,1,elapsed.total_seconds())

    a = 1000000
    elapsed = timeit.timeit(lambda: F2(i),number=a)
    measure2[i] = elapsed/a
    sheet1.write(i,3,i)
    sheet1.write(i,4,elapsed/a)

print(measure1)
print(measure2)
wb.save("PR2.xls")
