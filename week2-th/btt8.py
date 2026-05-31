# Bai 8: Can bac hai nguyen (khong dung sqrt)
def can_bac_hai(n):
    if n == 0:
        return 0
    trai = 1
    phai = n
    ket_qua = 0
    while trai <= phai:
        giua = (trai + phai) // 2
        if giua * giua <= n:
            ket_qua = giua  # ghi lai, tim so lon hon
            trai = giua + 1
        else:
            phai = giua - 1
    return ket_qua

print("Can bac hai nguyen cua 8 la:", can_bac_hai(8))
print("Can bac hai nguyen cua 16 la:", can_bac_hai(16))