# Bai 15: Tim k phan tu gan x nhat
def k_phan_tu_gan(a, k, x):
    trai = 0
    phai = len(a) - k
    while trai < phai:
        giua = (trai + phai) // 2
        # So sanh khoang cach tu hai dau cua cua so kich thuoc k
        if x - a[giua] > a[giua + k] - x:
            trai = giua + 1
        else:
            phai = giua
    return a[trai : trai + k]

a = [1, 2, 3, 4, 5]
k = 4
x = 3
print("K phan tu gan nhat:", k_phan_tu_gan(a, k, x))