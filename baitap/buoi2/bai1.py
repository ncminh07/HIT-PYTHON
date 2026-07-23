thang = int(input("Nhập tháng: "))
while thang < 1 or thang > 12 :
        thang = int(input("nhap lại tháng hợp lệ (1-12): "))
nam = int(input("Nhập năm: "))
while nam < 1 :
        nam = int(input("nhap lại năm hợp lệ (1-...): "))
namNhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
print()
if thang == 2:
    if namNhuan:
        print("Tháng 2 năm", nam, "có 29 ngày.")
    else:
        print("Tháng 2 năm", nam, "có 28 ngày.")
elif thang in [4, 6, 9, 11]:
    print("Tháng", thang, "năm", nam, "có 30 ngày.")
else:
    print("Tháng", thang, "năm", nam, "có 31 ngày.")
