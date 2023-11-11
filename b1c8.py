#8.1
a=float(input("Nhap so a : "))
b=float(input("Nhap so b : "))
c=float(input("Nhap so c : "))
d=float(input("Nhap so d : "))
max = a
if max < b: max = b
if max < c: max = c
if max < d: max = d
min = c
if min > a: min = a
if min > b: min = b
if min > d: min = d
print("gia tri lon nhat la : ", max)
print("gia tri nho nhat la : ", min)
