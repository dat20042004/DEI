# Bai 9: Vi tri chen vao de giu thu tu
def vi_tri_chen(a, x):
    trai = 0
    phai = len(a) - 1
    ket_qua = len(a)        # neu x lon hon tat ca, chen vao cuoi
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] >= x:
            ket_qua = giua  # ghi lai, tim vi tri nho hon ben trai
            phai = giua - 1
        else:
            trai = giua + 1
    return ket_qua

a = [1, 3, 5, 6]
x = 4
print("Vi tri can chen", x, "la:", vi_tri_chen(a, x))