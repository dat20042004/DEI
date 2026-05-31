# Bai 4: Vi tri xuat hien cuoi cung
def vi_tri_cuoi(a, x):
    trai = 0
    phai = len(a) - 1
    ket_qua = -1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            ket_qua = giua      # ghi lai vi tri, tim tiep ben phai
            trai = giua + 1
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return ket_qua

a = [1, 2, 2, 2, 3]
x = 2
print("Vi tri cuoi cung cua", x, "la:", vi_tri_cuoi(a, x))