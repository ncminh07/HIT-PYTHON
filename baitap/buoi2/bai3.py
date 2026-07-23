n = int(input("Nhập một số nguyên n : "))
while n < 0 :
    n = int(input("Nhập lại một số nguyên n : "))
soN = n;
sum = 0
tongchuSo = 0
if n == 0 :
    tongchuSo = 1
while n != 0 :
    sum += n % 10
    n //= 10
    tongchuSo += 1
print("Số chữ số của n là:", tongchuSo , ",tổng các chữ số của n là:", sum)
if soN < 2 :
    print(soN, " không phải là số nguyên tố.")
else :
    snt = True
    for i in range(2, int(soN ** 0.5) + 1) :
        if soN % i == 0 :
            snt = False
            break
    if snt :
        print(soN, "là số nguyên tố.")
    else :
        print(soN, "không phải là số nguyên tố.")