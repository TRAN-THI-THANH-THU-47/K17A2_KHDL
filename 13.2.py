
ten_noi_dung=input("nhập tên nội dung:")
print("Content of file:")
f=open("HumptyDumpty.txt",'r')
noi_dung=f.read()
print(noi_dung)
so_dong=len(noi_dung.splitlines())
so_tu=len(noi_dung.split())
so_ki_tu=len(noi_dung)
print('----Report:Lines/ Words/ Chars----')
print('lines:',so_dong,'words:',so_tu,'chars:',so_ki_tu)
f.close