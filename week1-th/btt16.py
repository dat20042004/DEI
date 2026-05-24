""" Bài 16. Phần tử gần x nhất
Cho mảng số và giá trị x. Viết hàm tìm phần tử trong mảng có giá trị gần x nhất (chênh lệch
tuyệt đối nhỏ nhất). Trả về giá trị và vị trí của phần tử đó."""
def tim_gan_nhat(a, x):
    vitri_gan_nhat = 0
    khoang_cach_nho_nhat = abs(a[0] - x)  # Tạm tính khoảng cách của thằng đầu tiên
    
    for i in range(1, len(a)):
        kc_hien_tai = abs(a[i] - x)
        if kc_hien_tai < khoang_cach_nho_nhat:
            khoang_cach_nho_nhat = kc_hien_tai  # Cập nhật kỷ lục khoảng cách mới
            vitri_gan_nhat = i
            
    return a[vitri_gan_nhat], vitri_gan_nhat 