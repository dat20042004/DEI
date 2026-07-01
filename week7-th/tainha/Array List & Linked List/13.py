khoang = [[1, 3], [2, 6], [8, 10]]
khoang.sort(key=lambda x: x[0]) # Sắp xếp theo điểm bắt đầu
ket_qua = [khoang[0]]

for bat_dau, ket_thuc in khoang[1:]:
    if bat_dau <= ket_qua[-1][1]:
        ket_qua[-1][1] = max(ket_qua[-1][1], ket_thuc) # Gộp khoảng
    else:
        ket_qua.append([bat_dau, ket_thuc])
print("Gộp khoảng:", ket_qua)