# Bai 11: Tim phan tu nho nhat trong mang bi xoay
def phan_tu_nho_nhat(a):
    trai = 0
    phai = len(a) - 1
    while trai < phai:
        giua = (trai + phai) // 2
        if a[giua] > a[phai]:
            trai = giua + 1     # phan nho nhat o ben phai
        else:
            phai = giua         # phan nho nhat o ben trai hoac chinh giua
    return a[trai]

a = [3, 4, 5, 1, 2]
print("Phan tu nho nhat la:", phan_tu_nho_nhat(a))