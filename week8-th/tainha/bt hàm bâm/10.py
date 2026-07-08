def ky_tu_doc_nhat(chuoi):
    dem = {}
    # Bước 1: Đếm tần suất
    for c in chuoi:
        dem[c] = dem.get(c, 0) + 1
        
    # Bước 2: Tìm ký tự đầu tiên có tần suất = 1
    for i, c in enumerate(chuoi):
        if dem[c] == 1:
            return i
    return -1

print("Bài 10:", ky_tu_doc_nhat('leetcode')) # Ký tự 'l' ở vị trí 0 [cite: 141]