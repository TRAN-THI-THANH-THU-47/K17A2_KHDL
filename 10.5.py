import re
def is_valid_zip(zip_code):
    if re.match(r"^d{6}$",zip_code):
        return True
    else:
        return False
zip_code=int(input("Nhập mã zip code:"))
if is_valid_zip(zip_code):
    print("Mã zip hợp lệ!!!")
else:
    print("Mã zip không hợp lệ")