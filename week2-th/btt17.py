# Bai 17: Tim suc chua tau nho nhat de chuyen hang trong D ngay
import math

def co_the_chuyen(w, suc_chua, D):
    so_ngay = 1
    trong_luong_hom_nay = 0
    for kien in w:
        if trong_luong_hom_nay + kien > suc_chua:
            so_ngay += 1            # sang ngay moi
            trong_luong_hom_nay = 0
        trong_luong_hom_nay += kien
    return so_ngay <= D

def suc_chua_nho_nhat(w, D):
    trai = max(w)       # toi thieu phai chua duoc kien nang nhat
    phai = sum(w)       # toi da la chuyen het trong 1 ngay
    ket_qua = phai
    while trai <= phai:
        giua = (trai + phai) // 2
        if co_the_chuyen(w, giua, D):
            ket_qua = giua
            phai = giua - 1
        else:
            trai = giua + 1
    return ket_qua

w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
print("Suc chua nho nhat:", suc_chua_nho_nhat(w, D))