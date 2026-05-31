# Bai 1: Tim kiem co ban
def tim_kiem(a, x):
    trai = 0
    phai = len(a) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            return giua
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return -1

a = [1, 3, 5, 7, 9]
x = 7
ket_qua = tim_kiem(a, x)
if ket_qua != -1:
    print("Tim thay x =", x, "tai vi tri:", ket_qua)
else:
    print("Khong tim thay x =", x)