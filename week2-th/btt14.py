# Bai 14: Tim x trong ma tran 2D
def tim_ma_tran(matrix, x):
    so_hang = len(matrix)
    so_cot = len(matrix[0])
    trai = 0
    phai = so_hang * so_cot - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        hang = giua // so_cot       # tinh hang tu vi tri giua
        cot = giua % so_cot         # tinh cot tu vi tri giua
        if matrix[hang][cot] == x:
            return True
        elif matrix[hang][cot] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return False

matrix = [[1, 3, 5], [7, 9, 11]]
x = 9
print("Ket qua tim", x, "la:", tim_ma_tran(matrix, x))