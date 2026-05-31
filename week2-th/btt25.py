# Bai 25: Dat m nam cham vao n gio sao cho luc tu nho nhat la lon nhat
def co_the_dat(x, m, khoang_cach_min):
    so_nam_cham = 1
    vi_tri_truoc = x[0]
    for i in range(1, len(x)):
        if x[i] - vi_tri_truoc >= khoang_cach_min:
            so_nam_cham += 1
            vi_tri_truoc = x[i]
    return so_nam_cham >= m

def luc_tu_lon_nhat(x, m):
    x.sort()
    trai = 1
    phai = x[-1] - x[0]
    ket_qua = 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if co_the_dat(x, m, giua):
            ket_qua = giua
            trai = giua + 1
        else:
            phai = giua - 1
    return ket_qua

x = [1, 2, 3, 4, 7]
m = 3
print("Luc tu lon nhat:", luc_tu_lon_nhat(x, m))