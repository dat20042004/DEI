# Bai 21: Chia mang thanh k doan, tong lon nhat la nho nhat
def co_the_chia(a, k, gioi_han):
    so_doan = 1
    tong = 0
    for so in a:
        if so > gioi_han:
            return False
        if tong + so > gioi_han:
            so_doan += 1
            tong = 0
        tong += so
    return so_doan <= k

def chia_mang(a, k):
    trai = max(a)
    phai = sum(a)
    ket_qua = phai
    while trai <= phai:
        giua = (trai + phai) // 2
        if co_the_chia(a, k, giua):
            ket_qua = giua
            phai = giua - 1
        else:
            trai = giua + 1
    return ket_qua

a = [7, 2, 5, 10, 8]
k = 2
print("Tong lon nhat nho nhat:", chia_mang(a, k))