a=input("nhập tên tập tin:")
from csv import reader
with open('dienthoai.csv','r') as read_obj:
    read_obj=open('dienthoai.csv','r')
    row=read_obj.read()
    print(row)