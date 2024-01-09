a=input("Nhập tên tập tin:")
from csv import reader
with open('Menu.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)