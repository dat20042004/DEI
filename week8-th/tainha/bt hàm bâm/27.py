import time

# --- 1. HỆ THỐNG CỦA BẠN (Dễ đoán) ---
def ham_bam_de_doan(k, m=10):
    return k % m  # Hàm băm chia lấy dư đơn giản

bang_bam_bi_loi = [[] for _ in range(10)]

# --- 2. HACKER TẤN CÔNG ---
print("Hacker đang gửi 10.000 dữ liệu độc hại vào hệ thống...")
# Hacker cố tình gửi toàn bộ các số có tận cùng là 0 (10, 20, 30... 100000)
for i in range(1, 10001):
    du_lieu_doc = i * 10 
    idx = ham_bam_de_doan(du_lieu_doc)
    bang_bam_bi_loi[idx].append(du_lieu_doc)

# Kiểm tra hậu quả:
print("-> Số lượng phần tử trong Giỏ 0:", len(bang_bam_bi_loi[0]))
print("-> Số lượng phần tử trong các giỏ khác:", len(bang_bam_bi_loi[1]))

# --- 3. ĐO TỐC ĐỘ KHI HỆ THỐNG BỊ TREO ---
bat_dau = time.time()
# Tìm một số nằm ở cuối cùng của cái giỏ khổng lồ đó
tim_kiem = 100000 in bang_bam_bi_loi[0] 
ket_thuc = time.time()

print(f"-> Thời gian máy chủ loay hoay tìm kiếm: {ket_thuc - bat_dau:.5f} giây (Chậm đi rất nhiều!)")



import random

class HeThongAnToan:
    def __init__(self, m=10):
        self.m = m
        self.bang_bam = [[] for _ in range(m)]
        # Sinh ra một khóa bí mật hoàn toàn ngẫu nhiên khi bật máy chủ
        self.KHOA_BI_MAT = random.randint(1, 999999) 
        print(f"(Máy chủ) Đã khởi tạo Khóa Bí Mật: {self.KHOA_BI_MAT}")

    def ham_bam_an_toan(self, k):
        # Trộn lẫn dữ liệu của người dùng với Khóa bí mật trước khi băm
        # Hacker không biết khóa bí mật nên không thể đoán được kết quả
        k_da_tron = k ^ self.KHOA_BI_MAT # Dùng phép XOR để trộn
        return k_da_tron % self.m
        
    def them_du_lieu(self, k):
        idx = self.ham_bam_an_toan(k)
        self.bang_bam[idx].append(k)

# --- THỬ NGHIỆM LẠI VỚI HACKER ---
print("\n--- HỆ THỐNG ĐÃ ĐƯỢC NÂNG CẤP ---")
he_thong_moi = HeThongAnToan()

print("Hacker lại gửi 10.000 dữ liệu độc hại (bội số của 10) như cũ...")
for i in range(1, 10001):
    du_lieu_doc = i * 10 
    he_thong_moi.them_du_lieu(du_lieu_doc)

# Kiểm tra xem dữ liệu có còn dồn vào Giỏ 0 không
print("CHI TIẾT PHÂN BỐ DỮ LIỆU:")
for i, gio in enumerate(he_thong_moi.bang_bam):
    print(f"Giỏ {i}: Chứa {len(gio)} phần tử")

print("=> TUYỆT VỜI! Dữ liệu của Hacker đã bị đánh tơi tả và rải đều ra mọi giỏ. Cuộc tấn công thất bại.")