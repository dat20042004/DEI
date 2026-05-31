# Bai 20: Tim so trang toi da nho nhat khi chia sach cho m hoc sinh
def co_the_chia(p, m, gioi_han):
    so_hs = 1
    tong = 0
    for sach in p:
        if sach > gioi_han:
            return False        # 1 cuon sach da vuot gioi han
        if tong + sach > gioi_han:
            so_hs += 1          # hoc sinh moi
            tong = 0
        tong += sach
    return so_hs <= m

def chia_sach(p, m):
    trai = max(p)       # toi thieu bang cuon sach day nhat
    phai = sum(p)       # toi da la tat ca cho 1 nguoi
    ket_qua = phai
    while trai <= phai:
        giua = (trai + phai) // 2
        if co_the_chia(p, m, giua):
            ket_qua = giua
            phai = giua - 1
        else:
            trai = giua + 1
    return ket_qua

p = [12, 34, 67, 90]
m = 2
print("So trang toi da nho nhat:", chia_sach(p, m))