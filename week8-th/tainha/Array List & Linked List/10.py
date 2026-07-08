a = [1, 3, 5]
b = [2, 4]
ket_qua = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        ket_qua.append(a[i])
        i += 1
    else:
        ket_qua.append(b[j])
        j += 1
ket_qua.extend(a[i:]) # Thêm các phần tử còn dư
ket_qua.extend(b[j:])
print("Trộn danh sách:", ket_qua)