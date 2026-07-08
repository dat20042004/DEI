import math

def ham_bam_nhan(k, m, A=0.6180339887):
    # k * A mod 1 chính là lấy phần thập phân.
    # Trong Python, có thể dùng phép chia lấy dư cho 1: (k * A) % 1
    phan_thap_phan = (k * A) % 1
    
    # Nhân với m và làm tròn xuống
    chi_so = math.floor(m * phan_thap_phan)
    return chi_so

# --- CHẠY THỬ ---
if __name__ == "__main__":
    m = 100 # Bảng băm có 100 giỏ
    khoa_1 = 12345
    khoa_2 = 12346 # Hai khóa sát nhau
    
    print(f"Khóa {khoa_1} rớt vào giỏ: {ham_bam_nhan(khoa_1, m)}")
    print(f"Khóa {khoa_2} rớt vào giỏ: {ham_bam_nhan(khoa_2, m)}")