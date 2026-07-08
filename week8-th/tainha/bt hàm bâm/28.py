def tim_ma_tran_con(ma_tran_lon, ma_tran_nho):
    p = len(ma_tran_nho)     # Số hàng của ma trận mẫu (Ví dụ: 2)
    q = len(ma_tran_nho[0])  # Số cột của ma trận mẫu (Ví dụ: 2)
    m = len(ma_tran_lon)     # Số hàng của ma trận lớn
    n = len(ma_tran_lon[0])  # Số cột của ma trận lớn

    if p > m or q > n: return -1

    CO_SO = 31
    MOD = 10**9 + 7

    # --- BƯỚC 1: HÀM BĂM 1 HÀNG NGANG (1D) ---
    def bam_hang(chuoi_ngang):
        h = 0
        for c in chuoi_ngang:
            h = (h * CO_SO + ord(c)) % MOD
        return h

    # --- BƯỚC 2: TÍNH MÃ BĂM CHO MA TRẬN MẪU (2D) ---
    hash_mau_2d = 0
    for hang in ma_tran_nho:
        hash_hang = bam_hang(hang) # Băm từng hàng thành 1 số
        # Gộp các số đó lại thành 1 mã băm duy nhất (Băm dọc)
        hash_mau_2d = (hash_mau_2d * CO_SO + hash_hang) % MOD
        
    print(f"Mã băm của ma trận cần tìm: {hash_mau_2d}\n" + "-"*30)

    # Hệ số to nhất để phục vụ việc trượt dọc (giống bài 6)
    he_so_doc = 1
    for _ in range(p - 1):
        he_so_doc = (he_so_doc * CO_SO) % MOD

    # --- BƯỚC 3: QUÉT QUA MA TRẬN LỚN ---
    # Di chuyển cửa sổ ngang từng cột một (j)
    for j in range(n - q + 1):
        
        # 3a. Tính mã băm cho cửa sổ dọc đầu tiên (Nằm sát mép trên cùng)
        hash_cua_so_2d = 0
        for i in range(p):
            doan_ngang = ma_tran_lon[i][j : j+q]
            hash_cua_so_2d = (hash_cua_so_2d * CO_SO + bam_hang(doan_ngang)) % MOD
            
        if hash_cua_so_2d == hash_mau_2d:
            return (0, j) # Tìm thấy ngay ô đầu tiên!

        # 3b. ROLLING HASH THEO CỘT (Trượt dọc xuống dưới)
        for i in range(1, m - p + 1):
            # Lấy đoạn ngang bị rớt lại phía trên
            hang_bi_loai = ma_tran_lon[i - 1][j : j+q]
            hash_loai = bam_hang(hang_bi_loai)
            
            # Lấy đoạn ngang mới lọt vào cửa sổ ở phía dưới
            hang_vao_moi = ma_tran_lon[i + p - 1][j : j+q]
            hash_moi = bam_hang(hang_vao_moi)

            # Cập nhật mã băm 2D siêu tốc (Trừ cái cũ, cộng cái mới)
            hash_cua_so_2d = (hash_cua_so_2d - hash_loai * he_so_doc) % MOD
            hash_cua_so_2d = (hash_cua_so_2d * CO_SO + hash_moi) % MOD
            
            # Xử lý số âm do phép trừ
            if hash_cua_so_2d < 0:
                hash_cua_so_2d += MOD

            # So sánh
            if hash_cua_so_2d == hash_mau_2d:
                return (i, j) # (Hàng i, Cột j)

    return -1

# --- CHẠY THỬ NGHIỆM ---
if __name__ == "__main__":
    # Ma trận lớn (4x4)
    anh_lon = [
        "abcd",
        "efgh",
        "ijxy",
        "mnzt"
    ]
    
    # Khối cần tìm (2x2)
    anh_nho = [
        "xy",
        "zt"
    ]
    
    print("Đang tìm kiếm ma trận...")
    ket_qua = tim_ma_tran_con(anh_lon, anh_nho)
    
    if ket_qua != -1:
        hang, cot = ket_qua
        print(f"-> TÌM THẤY! Ma trận con bắt đầu từ Tọa độ: Hàng {hang}, Cột {cot}")
    else:
        print("-> Không tìm thấy ma trận con.")