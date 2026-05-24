'''Bài 8. Đếm số lần xuất hiện
Viết hàm dem_xuat_hien(a, x) đếm số lần x xuất hiện trong mảng'''
def dem_xuat_hien(a, x):
    dem = 0  # Tạo một cái hộp đếm, ban đầu bằng 0
    for i in range(len(a)):
        if a[i] == x:
            dem = dem + 1  # Mỗi lần thấy x thì cộng thêm 1 vào hộp
    return dem  # Duyệt hết mảng mới trả về kết quả đếm