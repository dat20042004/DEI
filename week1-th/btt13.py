'''Bài 13. Tìm kiếm trên chuỗi
Cho danh sách tên sinh viên (kiểu chuỗi). Viết hàm tìm xem một tên có trong danh sách
không, không phân biệt chữ hoa/thường, trả về vị trí tìm thấy hoặc -1'''
def tim_ten(ds, ten_can_tim):
    for i in range(len(ds)):
        # Biến đổi cả hai tên về dạng viết thường rồi mới so sánh
        if ds[i].lower() == ten_can_tim.lower():
            return i
    return -1