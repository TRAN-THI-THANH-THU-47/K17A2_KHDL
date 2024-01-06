import datetime
ngay=int(input("Nhập ngày:"))
thang=int(input("Nhập tháng:"))
nam=int(input("Nhập năm:"))
ngay_hop_le=True
if ngay_hop_le:
    ngay_thang_nam=datetime.datetime(nam,thang,ngay)
    ngay_formatted=ngay_thang_nam.strftime("%d-%m-%Y")
    print("Ngày:",ngay_formatted)
    if nam%4==0 and (nam % 100!=0 or nam %400==0):
        print("Là năm nhuận")
    else:
        print("Không phải năm nhuận")
    thu=ngay_thang_nam.strftime("%A")
    print("Ngày/tháng/năm đó là thứ:",thu)
    so_ngay=(datetime.datetime(nam,thang+1,1)-datetime.datetime(nam,thang,1)).days
    print("Tháng",thang,"có",so_ngay,"ngày.")
else:
    print("Ngày tháng năm không hợp lệ!!!")