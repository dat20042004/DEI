# Bai 16: Tim toc do an nho nhat de an het trong h gio
import math

def co_the_an_het(pile, s, h):
    tong_gio = 0
    for dong in pile:
        tong_gio += math.ceil(dong / s)  # so gio can cho tung dong
    return tong_gio <= h

def toc_do_nho_nhat(pile, h):
    trai = 1
    phai = max(pile)    # toc do lon nhat can la dong lon nhat
    ket_qua = phai
    while trai <= phai:
        giua = (trai + phai) // 2
        if co_the_an_het(pile, giua, h):
            ket_qua = giua  # ghi lai, thu toc do nho hon
            phai = giua - 1
        else:
            trai = giua + 1
    return ket_qua

pile = [3, 6, 7, 11]
h = 8
print("Toc do an nho nhat:", toc_do_nho_nhat(pile, h))