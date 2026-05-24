'''Bài 9. Tìm tất cả vị trí
Viết hàm tim_tat_ca(a, x) trả về danh sách tất cả các chỉ số mà x xuất hiện. Nếu không
có, trả về danh sách rỗng'''
# 1. Định nghĩa hàm
def tim_tat_ca(a, x):
    danh_sach_vi_tri = [] 
    for i in range(len(a)):
        if a[i] == x:
            danh_sach_vi_tri.append(i)
    return danh_sach_vi_tri

# 2. Tạo dữ liệu thực tế để chạy thử
mang_a = [4, 1, 4, 9, 4]
so_x = 4

# 3. Gọi hàm và lệnh print để in kết quả ra màn hình
ket_qua = tim_tat_ca(mang_a, so_x)
print(ket_qua)