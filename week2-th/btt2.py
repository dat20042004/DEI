# Bai 2: Kiem tra ton tai
def kiem_tra(a, x):
    trai = 0
    phai = len(a) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if a[giua] == x:
            return True
        elif a[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return False

a = [2, 4, 6, 8]
x = 5
print("Ket qua:", kiem_tra(a, x))