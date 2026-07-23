n = int(input("Nhập số tiền bạn có : "))

while n < 0 :
    n = int(input("Nhập lại số tiền bạn có : "))

soChai = n // 28
if soChai in (0,1, 2):
    print("Bạn có thể mua", soChai, "chai bia.")
elif soChai >= 3 : 
    vo = soChai
    sochaiThem = soChai // 3
    soChai += sochaiThem
    print(f"Bạn có thể mua {soChai} chai bia. ( mua {vo} chai,dư {vo} vỏ đổi thành {sochaiThem} nữa )")
