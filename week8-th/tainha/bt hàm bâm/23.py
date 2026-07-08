def tinh_chi_square(danh_sach_dem, tong_so_khoa, so_gio):
    # E: Số lượng phần tử lý tưởng cho mỗi giỏ
    E = tong_so_khoa / so_gio 
    diem_chi_square = 0
    
    # O: Số lượng phần tử thực tế trong từng giỏ
    for O in danh_sach_dem:
        diem_chi_square += ((O - E) ** 2) / E
        
    return diem_chi_square

def danh_gia_ham_bam():
    # 1. Chuẩn bị 100 từ khóa (giả lập bằng cách tạo chuỗi ngẫu nhiên)
    # Ví dụ: "tu_0", "tu_1", ..., "tu_99"
    tap_khoa = [f"tu_{i}" for i in range(100)]
    tong_so_khoa = len(tap_khoa)
    so_gio = 10 # Ta có 10 cái giỏ
    
    # Tạo các mảng để đếm số phần tử rớt vào từng giỏ (Ban đầu toàn số 0)
    dem_ham_te = [0] * so_gio
    dem_ham_tot = [0] * so_gio
    
    # 2. Hai hàm băm để thi đấu
    def ham_bam_te(chuoi):
        # Hàm tệ: Chỉ lấy độ dài chuỗi chia lấy dư. 
        # Vì các chữ "tu_1", "tu_9" có độ dài giống hệt nhau, chúng sẽ dồn vào 1 chỗ.
        return len(chuoi) % so_gio
        
    def ham_bam_tot(chuoi):
        # Hàm tốt: Lấy tổng mã ASCII nhân với cơ số nguyên tố (Polynomial)
        tong = 0
        for c in chuoi:
            tong = (tong * 31 + ord(c))
        return tong % so_gio

    # 3. Tiến hành phân loại dữ liệu vào giỏ
    for khoa in tap_khoa:
        idx_te = ham_bam_te(khoa)
        dem_ham_te[idx_te] += 1
        
        idx_tot = ham_bam_tot(khoa)
        dem_ham_tot[idx_tot] += 1

    # 4. Tính điểm Chi-square
    diem_te = tinh_chi_square(dem_ham_te, tong_so_khoa, so_gio)
    diem_tot = tinh_chi_square(dem_ham_tot, tong_so_khoa, so_gio)
    
    # 5. In kết quả
    print("--- HÀM BĂM TỆ (Chỉ lấy độ dài chuỗi) ---")
    print(f"Phân bố thực tế : {dem_ham_te}")
    print(f"Lý tưởng        : Mỗi giỏ chứa {tong_so_khoa/so_gio} phần tử")
    print(f"Điểm Chi-square : {diem_te} (Điểm rất cao -> Va chạm cực mạnh, dồn cục)")
    
    print("\n--- HÀM BĂM TỐT (Mã hóa đa thức) ---")
    print(f"Phân bố thực tế : {dem_ham_tot}")
    print(f"Lý tưởng        : Mỗi giỏ chứa {tong_so_khoa/so_gio} phần tử")
    print(f"Điểm Chi-square : {diem_tot} (Điểm thấp -> Phân bố đồng đều, rất cân bằng)")
    
    print("\n=> KẾT LUẬN: Hàm băm Đa thức tốt hơn rất nhiều!")

# --- CHẠY THỬ ---
if __name__ == "__main__":
    danh_gia_ham_bam()