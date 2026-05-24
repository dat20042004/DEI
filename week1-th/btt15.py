""" Bài 15. Tìm số nguyên tố đầu tiên
Cho mảng số nguyên dương. Viết hàm tìm số nguyên tố đầu tiên trong mảng, trả về giá trị
và vị trí của nó. Gợi ý: viết thêm hàm phụ kiểm tra số nguyên tố."""
# Hàm phụ kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):  # Kiểm tra xem n có chia hết cho số nào từ 2 đến n-1 không
        if n % i == 0:
            return False  # Chia hết là không phải số nguyên tố
    return True

# Hàm chính
def tim_so_nguyen_to_dau(a):
    for i in range(len(a)):
        if la_so_nguyen_to(a[i]):  # Gọi hàm phụ ở đây
            return a[i], i  # Trả về cả giá trị và vị trí theo yêu cầu [cite: 74]
    return None, -1