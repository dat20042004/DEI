def rabin_karp(van_ban, mau):
    n = len(van_ban) # Độ dài văn bản (VD: 'zabcd' là 5)
    m = len(mau)     # Độ dài từ khóa cần tìm (VD: 'abc' là 3)
    
    if m == 0 or n < m:
        return -1
        
    p = 31 # Cơ số (giống Bài 3)
    q = 1000000009 # Số nguyên tố lớn để chia lấy dư (Modulo)
    
    # 1. Tính hệ số p^(m-1) để dùng cho việc trừ chữ cái rớt khỏi cửa sổ
    # Trọng số của chữ cái đứng đầu tiên trong cửa sổ
    he_so_to_nhat = 1
    for _ in range(m - 1):
        he_so_to_nhat = (he_so_to_nhat * p) % q
        
    hash_mau = 0
    hash_cua_so = 0
    
    # 2. Băm từ khóa và Băm "cửa sổ" đầu tiên của văn bản
    for i in range(m):
        hash_mau = (hash_mau * p + ord(mau[i])) % q
        hash_cua_so = (hash_cua_so * p + ord(van_ban[i])) % q
        
    print(f"Mã băm của từ khóa cần tìm: {hash_mau}")
        
    # 3. Bắt đầu trượt cửa sổ trên văn bản
    for i in range(n - m + 1):
        chuoi_trong_cua_so = van_ban[i : i+m]
        print(f"Cửa sổ hiện tại: '{chuoi_trong_cua_so}' - Mã băm: {hash_cua_so}")
        
        # Nếu mã băm khớp nhau
        if hash_mau == hash_cua_so:
            # Kiem tra lại từng chữ cho chắc ăn (phòng trường hợp va chạm băm)
            if chuoi_trong_cua_so == mau:
                return i # Tìm thấy! Trả về vị trí
                
        # Nếu chưa tìm thấy và chưa đến cuối văn bản -> TRƯỢT CỬA SỔ
        if i < n - m:
            ky_tu_bi_loai = ord(van_ban[i])       # Chữ cái rớt lại phía sau
            ky_tu_vao_moi = ord(van_ban[i + m])   # Chữ cái mới lọt vào cửa sổ
            
            # Công thức Rolling Hash siêu tốc:
            # 1. Trừ đi ký tự bị loại (nhân với hệ số to nhất của nó)
            hash_cua_so = (hash_cua_so - ky_tu_bi_loai * he_so_to_nhat) % q
            # 2. Dịch các ký tự còn lại lên 1 bậc (nhân p) và cộng ký tự mới vào
            hash_cua_so = (hash_cua_so * p + ky_tu_vao_moi) % q
            
            # Đảm bảo mã băm không bị âm (do phép trừ ở trên)
            if hash_cua_so < 0:
                hash_cua_so += q
                
    return -1 # Trượt hết văn bản mà không thấy

# --- CHẠY THỬ VÍ DỤ ---
if __name__ == "__main__":
    van_ban = "zabcd"
    mau = "abc"
    
    print(f"Đang tìm '{mau}' trong '{van_ban}'...\n" + "-"*30)
    vi_tri = rabin_karp(van_ban, mau)
    
    print("-"*30)
    if vi_tri != -1:
        print(f"-> THÀNH CÔNG: Đã tìm thấy '{mau}' bắt đầu từ vị trí thứ {vi_tri} (Index {vi_tri})")
    else:
        print("-> KHÔNG TÌM THẤY!")