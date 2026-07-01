def phan_tu_chung(mang1, mang2):
    set1 = set(mang1) # Chuyển mảng 1 thành Tập băm (Set)
    ket_qua = []
    for x in mang2:
        if x in set1: # Tìm kiếm trong Set cực nhanh: O(1)
            ket_qua.append(x)
    return set(ket_qua) # Trả về set để lọc trùng

print("Bài 4:", phan_tu_chung([1,2,3], [2,3,4])) # {2, 3} [cite: 120]