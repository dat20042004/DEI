# Bai 24: Them k tram xang, giam khoang cach lon nhat
import math

def dem_tram_can_them(x, khoang_cach_max):
    so_tram = 0
    for i in range(1, len(x)):
        khoang = x[i] - x[i-1]
        # Can them bao nhieu tram vao khoang nay
        so_tram += math.ceil(khoang / khoang_cach_max) - 1
    return so_tram

def khoang_cach_lon_nhat(x, k):
    trai = 0.0
    phai = x[-1] - x[0]
    # Tim kiem nhi phan tren so thuc
    for _ in range(100):    # lap 100 lan la du chinh xac
        giua = (trai + phai) / 2
        if dem_tram_can_them(x, giua) <= k:
            phai = giua     # co the giam khoang cach nho hon
        else:
            trai = giua
    return round(phai, 6)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
print("Khoang cach lon nhat:", khoang_cach_lon_nhat(x, k))