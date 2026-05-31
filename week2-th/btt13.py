# Bai 13: Tim phan tu xuat hien 1 lan trong mang doi
def phan_tu_don(a):
    trai = 0
    phai = len(a) - 1
    while trai < phai:
        giua = (trai + phai) // 2
        # Dam bao giua la chi so chan
        if giua % 2 == 1:
            giua -= 1
        if a[giua] == a[giua + 1]:
            trai = giua + 2     # phan don o ben phai
        else:
            phai = giua         # phan don o ben trai hoac chinh giua
    return a[trai]

a = [1, 1, 2, 3, 3, 4, 4]
print("Phan tu don le la:", phan_tu_don(a))