# Cài đặt hàm băm cho chuỗi bằng tổng mã ký tự
def ham_bam_chuoi(chuoi, m):
    tong = 0
    print(f"--- Đang băm chuỗi '{chuoi}' ---")
    
    # Duyệt qua từng chữ cái trong chuỗi
    for ky_tu in chuoi:
        ma_ascii = ord(ky_tu) # Lấy mã số ASCII của chữ cái
        tong += ma_ascii
        print(f" Ký tự '{ky_tu}' -> Mã số: {ma_ascii}")
        
    # Lấy tổng chia dư cho kích thước bảng (m)
    chi_so = tong % m
    print(f"Tổng các mã số = {tong}")
    print(f"Vị trí Bucket (Tổng % {m}) = {chi_so}\n")
    
    return chi_so

if __name__ == "__main__":
    m = 10 # Giả sử bảng băm có 10 giỏ (từ 0 đến 9)
    
    # Thử nghiệm với ví dụ của đề bài
    hash_1 = ham_bam_chuoi("abc", m)
    hash_2 = ham_bam_chuoi("cba", m)
    
    print("NHƯỢC ĐIỂM CỦA HÀM BĂM NÀY:")
    if hash_1 == hash_2:
        print("-> Chuỗi 'abc' và 'cba' đều có chung mã băm (Hash)!")