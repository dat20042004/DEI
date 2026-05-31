# Bai 6: Lower Bound - phan tu nho nhat >= x
def lower_bound(a, x):
    trai = 0
    phai = len(a) - 1
    ket_qua = len(a)        # mac dinh tra ve n neu khong co
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] >= x:
            ket_qua = giua  # ghi lai, tim tiep ben trai
            phai = giua - 1
        else:
            trai = giua + 1
    return ket_qua

a = [1, 3, 5, 7]
x = 4
vi_tri = lower_bound(a, x)
print("Chi so Lower Bound cua", x, "la:", vi_tri)