# Bai 19: Tim khoang cach lon nhat khi dat bo vao chuong
def co_the_dat(x, c, khoang_cach_min):
    so_bo = 1
    cuong_truoc = x[0]
    for i in range(1, len(x)):
        if x[i] - cuong_truoc >= khoang_cach_min:
            so_bo += 1
            cuong_truoc = x[i]
    return so_bo >= c

def khoang_cach_lon_nhat(x, c):
    x.sort()
    trai = 1
    phai = x[-1] - x[0]    # khoang cach lon nhat co the
    ket_qua = 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if co_the_dat(x, c, giua):
            ket_qua = giua  # ghi lai, thu khoang cach lon hon
            trai = giua + 1
        else:
            phai = giua - 1
    return ket_qua

x = [1, 2, 4, 8, 9]
c = 3
print("Khoang cach lon nhat:", khoang_cach_lon_nhat(x, c))