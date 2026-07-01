arr = [3, 1, 3, 2, 1]
da_thay = set()
ket_qua = []
for so in arr:
    if so not in da_thay:
        da_thay.add(so)
        ket_qua.append(so)
print("Loại trùng lặp:", ket_qua)