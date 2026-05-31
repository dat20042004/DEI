# Bai 18: Tim so nguyen duong thu k bi thieu
def phan_tu_thu_k_thieu(a, k):
    trai = 0
    phai = len(a) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        # So so bi thieu truoc vi tri giua: a[giua] - (giua+1)
        so_thieu = a[giua] - (giua + 1)
        if so_thieu < k:
            trai = giua + 1
        else:
            phai = giua - 1
    # So thu k bi thieu = trai + k
    return trai + k

a = [2, 3, 4, 7, 11]
k = 5
print("So nguyen duong thu", k, "bi thieu la:", phan_tu_thu_k_thieu(a, k))