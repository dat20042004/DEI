''' Bài 19. Tìm kiếm theo khóa (dữ liệu có cấu trúc)
Cho danh sách sinh viên, mỗi sinh viên gồm: mã SV, họ tên, điểm trung bình (dùng
dictionary hoặc class). Viết hàm tìm sinh viên theo mã SV và in đầy đủ thông tin của sinh
viên đó; thông báo phù hợp nếu không tìm thấy'''
def tim_sinh_vien(ds_sinh_vien, ma_can_tim):
    for sv in ds_sinh_vien:
        # sv là một từ điển chứa thông tin 1 sinh viên
        if sv["ma_sv"] == ma_can_tim:
            print("--- Thông tin sinh viên tìm thấy ---") [cite: 91]
            print("Mã SV:", sv["ma_sv"]) [cite: 91]
            print("Họ tên:", sv["ho_ten"]) [cite: 91]
            print("Đểm TB:", sv["diem_tb"]) [cite: 91]
            return  # In xong rồi thì dừng hàm luôn
            
    print("Không tìm thấy sinh viên có mã này!") 