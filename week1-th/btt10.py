'''Bài 10. Vị trí xuất hiện cuối cùng
Viết hàm trả về vị trí xuất hiện cuối cùng của x trong mảng (trả về -1 nếu không có). Gợi
ý: duyệt từ cuối mảng về đầu, hoặc cập nhật biến lưu vị trí khi duyệt từ đầu'''
def vi_tri_cuoi_cung(a, x):
    # len(a) - 1 là vị trí cuối cùng. Duyệt lùi về -1 (nghĩa là dừng ở 0), mỗi bước trừ 1 (-1)
    for i in range(len(a) - 1, -1, -1):
        if a[i] == x:
            return i  # Gặp phát đầu tiên khi đi lùi chính là thằng cuối cùng trong mảng
    return -1