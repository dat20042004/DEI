# Bai 10: Tim trong mang bi xoay
def tim_mang_xoay(a, x):
    trai = 0
    phai = len(a) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            return giua
        # Kiem tra nua trai co dang tang deu khong
        if a[trai] <= a[giua]:
            if a[trai] <= x < a[giua]:
                phai = giua - 1     # tim ben trai
            else:
                trai = giua + 1     # tim ben phai
        else:
            if a[giua] < x <= a[phai]:
                trai = giua + 1     # tim ben phai
            else:
                phai = giua - 1     # tim ben trai
    return -1

a = [4, 5, 6, 7, 0, 1, 2]
x = 0
print("Vi tri cua", x, "la:", tim_mang_xoay(a, x))