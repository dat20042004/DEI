''' Bài 7. Kiểm tra tồn tại
Viết hàm ton_tai(a, x) trả về True nếu x có mặt trong mảng, ngược lại trả về False
(không dùng toán tử in có sẵn)'''
def ton_tai(a, x):
    # duyệt qua từng phần tử trong mảng
    for i in range(len(a)):
        if a[i] == x:   # nếu tìm thấy
            return True
    return False        # nếu duyệt hết mà không thấy