a=float(input("Nhap canh tam giac thu nhat : "))
b=float(input("Nhap canh tam giac thu hai : "))
c=float(input("Nhap canh tam giac thu ba : "))
cv=a+b+c
p=cv/2
import math
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Chu vi =" , cv)
print("Dien tich =" , s)

