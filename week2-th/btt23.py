# Bai 23: Tim phan tu nho thu k trong ma tran sap xep
def dem_nho_hon_bang(matrix, mid, n):
    so_luong = 0
    hang = n - 1
    cot = 0
    while hang >= 0 and cot < n:
        if matrix[hang][cot] <= mid:
            so_luong += hang + 1    # ca cot nay den hang hien tai
            cot += 1
        else:
            hang -= 1
    return so_luong

def phan_tu_thu_k(matrix, k):
    n = len(matrix)
    trai = matrix[0][0]
    phai = matrix[n-1][n-1]
    while trai < phai:
        giua = (trai + phai) // 2
        if dem_nho_hon_bang(matrix, giua, n) >= k:
            phai = giua
        else:
            trai = giua + 1
    return trai

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print("Phan tu nho thu", k, "la:", phan_tu_thu_k(matrix, k))