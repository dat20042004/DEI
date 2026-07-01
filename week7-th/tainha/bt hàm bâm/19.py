def dem_va_cham(tap_khoa, m, ham_bam):
    """
    tap_khoa: Danh sách các dữ liệu cần băm.
    m: Số lượng bucket (kích thước bảng băm).
    ham_bam: Hàm băm được sử dụng.
    """
    # Bước 1: Tạo các giỏ trống
    buckets = [[] for _ in range(m)]
    
    # Bước 2: Băm từng khóa và nhét vào giỏ
    for khoa in tap_khoa:
        idx = ham_bam(khoa, m)
        buckets[idx].append(khoa)
        
    tong_so_cap_va_cham = 0
    
    # Bước 3: Đi từng giỏ để đếm số cặp va chạm
    print("CHI TIẾT PHÂN BỐ:")
    for i, gio in enumerate(buckets):
        n = len(gio) # Số phần tử trong giỏ
        
        if n > 1:
            # Tính số cặp theo công thức n * (n - 1) / 2
            so_cap = (n * (n - 1)) // 2
            tong_so_cap_va_cham += so_cap
            print(f" -> Giỏ {i} có {n} phần tử {gio}. Phát sinh {so_cap} cặp va chạm.")
        elif n == 1:
            print(f" -> Giỏ {i} có {n} phần tử {gio}. An toàn, không va chạm.")
            
    print("-" * 40)
    return tong_so_cap_va_cham

# --- CHẠY THỬ THỰC TẾ ---
if __name__ == "__main__":
    # Định nghĩa một hàm băm đơn giản (lấy độ dài chuỗi chia dư cho m)
    def ham_bam_do_dai(chuoi, m):
        return len(chuoi) % m
        
    # Tập dữ liệu đầu vào
    danh_sach_tu = ["apple", "banana", "cat", "dog", "elephant", "fox", "ant"]
    so_gio = 5
    
    print("ĐÁNH GIÁ HÀM BĂM THEO ĐỘ DÀI CHUỖI:")
    tong_va_cham = dem_va_cham(danh_sach_tu, so_gio, ham_bam_do_dai)
    
    print(f"TỔNG KẾT: Hàm băm này tạo ra tổng cộng {tong_va_cham} cặp va chạm.")