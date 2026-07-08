
"""
CÂU 1 - Chia mảng (ứng dụng Tìm kiếm nhị phân)

Đề bài: W = [1,2,...,10], K = 5 xe. Mỗi xe chỉ chở các kiện hàng liên tiếp
nhau trong danh sách. Tìm tải trọng tối thiểu của 1 xe sao cho chở hết
hàng trong 1 lượt, và chia kiện hàng cho từng xe.
"""

# Ý tưởng: "Nhị phân trên đáp án" - đáp án (tải trọng tối thiểu) nằm trong
# đoạn [max(W), sum(W)]. Với mỗi giá trị tải trọng thử nghiệm, ta đếm xem
# cần bao nhiêu xe để chở hết hàng (tham lam: chất đầy xe hiện tại tới khi
# không chất thêm được nữa thì chuyển sang xe mới). Nếu số xe cần <= K thì
# tải trọng thử đó KHẢ THI -> thử giảm xuống; ngược lại phải tăng lên.

def dem_so_xe_can(w, tai_trong):
    so_xe = 1
    tong_hien_tai = 0
    for kien in w:
        if tong_hien_tai + kien > tai_trong:
            so_xe += 1
            tong_hien_tai = kien
        else:
            tong_hien_tai += kien
    return so_xe


def tim_tai_trong_toi_thieu(w, k):
    lo, hi = max(w), sum(w)
    while lo < hi:
        mid = (lo + hi) // 2
        if dem_so_xe_can(w, mid) <= k:
            hi = mid          # mid khả thi -> thử tải trọng nhỏ hơn
        else:
            lo = mid + 1       # mid không đủ -> phải tăng tải trọng
    return lo


def chia_kien_hang_cho_xe(w, tai_trong):
    """Chia W thành từng nhóm kiện hàng liên tiếp cho mỗi xe, dựa trên tai_trong đã tìm được."""
    danh_sach_xe = []
    nhom_hien_tai = []
    tong_hien_tai = 0
    for kien in w:
        if tong_hien_tai + kien > tai_trong:
            danh_sach_xe.append(nhom_hien_tai)
            nhom_hien_tai = [kien]
            tong_hien_tai = kien
        else:
            nhom_hien_tai.append(kien)
            tong_hien_tai += kien
    danh_sach_xe.append(nhom_hien_tai)
    return danh_sach_xe


if __name__ == "__main__":
    w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 5
    tai_trong = tim_tai_trong_toi_thieu(w, k)
    cach_chia = chia_kien_hang_cho_xe(w, tai_trong)

    print("Tải trọng tối thiểu =", tai_trong)
    print("Cách chia cho", len(cach_chia), "xe:")
    for i, xe in enumerate(cach_chia, 1):
        print(f"  Xe {i}: {xe} (tổng = {sum(xe)})")