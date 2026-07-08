# 1. Định nghĩa hàm băm (Chia lấy dư)
def ham_bam_modulo(k, m):
    """
    k: Khóa (chìa khóa / dữ liệu đầu vào là số nguyên)
    m: Số lượng bucket (kích thước của bảng băm)
    """
    return k % m

if __name__ == "__main__":
    # Đề bài ví dụ: k = 37, m = 10
    k_vi_du = 37
    m = 10
    chi_so = ham_bam_modulo(k_vi_du, m)
    print(f"Ví dụ của đề: Khóa {k_vi_du} đưa vào hàm băm (m={m}) sẽ ra chỉ số (bucket) là: {chi_so}")
    print("-" * 40)

    # 2. Quan sát phân bố cho một tập khóa
    # Giả sử ta có một danh sách các số nguyên lộn xộn
    tap_khoa = [15, 22, 37, 40, 55, 62, 77, 89, 91, 12, 105]
    
    # Tạo 10 cái "giỏ" (bucket) rỗng (từ số 0 đến 9)
    buckets = [[] for _ in range(m)]

    # Băm từng khóa và nhét vào giỏ tương ứng
    for khoa in tap_khoa:
        idx = ham_bam_modulo(khoa, m)
        buckets[idx].append(khoa)

    # 3. In kết quả để xem chúng được phân bố như thế nào
    print("QUAN SÁT SỰ PHÂN BỐ DỮ LIỆU:")
    for i in range(m):
        print(f"Bucket {i}: {buckets[i]}")