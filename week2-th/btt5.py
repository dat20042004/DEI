# Bai 5: Dem so lan xuat hien
def vi_tri_dau(a, x):
    trai = 0
    phai = len(a) - 1
    ket_qua = -1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            ket_qua = giua
            phai = giua - 1
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return ket_qua

def vi_tri_cuoi(a, x):
    trai = 0
    phai = len(a) - 1
    ket_qua = -1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            ket_qua = giua
            trai = giua + 1
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return ket_qua

def dem_so_lan(a, x):
    dau = vi_tri_dau(a, x)
    if dau == -1:
        return 0
    cuoi = vi_tri_cuoi(a, x)
    return cuoi - dau + 1

a = [1, 2, 2, 2, 3]
x = 2
print("So lan xuat hien cua", x, "la:", dem_so_lan(a, x))