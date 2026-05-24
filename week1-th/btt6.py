''' Bài 6. Hàm tìm kiếm cơ bản
Viết hàm linear_search(a, x) trả về vị trí đầu tiên của x trong mảng a, trả về -1 nếu
không có. Viết chương trình nhập mảng, nhập x và in kết quả ra màn hình.'''
def linear_search(a, x):
    # len(a) giúp lấy ra số lượng phần tử của mảng a
    for i in range(len(a)):
        if a[i] == x:
            return i  # Tìm thấy là trả về vị trí ngay và thoát hàm
    return -1  # Chạy hết vòng lặp phía trên mà không thoát nghĩa là không có

# Chạy thử chương trình
mang = [7, 3, 9, 12, 5, 8, 1]
can_tim = 5
ket_qua = linear_search(mang, can_tim)
print("Vị trí tìm thấy:", ket_qua)
