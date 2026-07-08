def nhom_theo_chu_cai_dau(danh_sach_tu):
    nhom = {}
    for tu in danh_sach_tu:
        chu_dau = tu[0] # Lấy chữ cái đầu làm khóa [cite: 123]
        if chu_dau not in nhom:
            nhom[chu_dau] = [] # Nếu chưa có, tạo list mới
        nhom[chu_dau].append(tu)
    return nhom

print("Bài 5:", nhom_theo_chu_cai_dau(["apple", "ant", "banana", "cat"]))