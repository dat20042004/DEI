# Bai 12: Tim dinh (lon hon ca hai hang xom)
def tim_dinh(a):
    trai = 0
    phai = len(a) - 1
    while trai < phai:
        giua = (trai + phai) // 2
        if a[giua] < a[giua + 1]:
            trai = giua + 1     # dinh o ben phai
        else:
            phai = giua         # dinh o ben trai hoac chinh giua
    return trai

a = [1, 2, 3, 1]
vi_tri = tim_dinh(a)
print("Vi tri dinh la:", vi_tri, "| Gia tri:", a[vi_tri])