import random

class BamPhoQuat:
    def __init__(self, m, p=1000000007):
        """
        m: Kích thước bảng băm
        p: Số nguyên tố cực lớn (Mặc định dùng 1.000.000.007)
        """
        self.m = m
        self.p = p
        
        # Bốc thăm ngẫu nhiên hệ số a và b mỗi lần chạy
        self.a = random.randint(1, self.p - 1) # a phải lớn hơn 0
        self.b = random.randint(0, self.p - 1)
        
        print(f"Hệ thống vừa tạo khóa bí mật ngẫu nhiên: a = {self.a}, b = {self.b}")

    def get_hash(self, k):
        # Áp dụng đúng công thức: h(k) = ((a*k + b) % p) % m
        gia_tri = ((self.a * k + self.b) % self.p) % self.m
        return gia_tri

# --- CHẠY THỬ NGHIỆM ---
if __name__ == "__main__":
    # Giả sử bảng băm có 10 giỏ
    m = 10 
    khoa_can_bam = 9999
    
    print("--- LẦN KHỞI ĐỘNG 1 ---")
    bang_1 = BamPhoQuat(m)
    print(f"Khóa {khoa_can_bam} rớt vào giỏ số: {bang_1.get_hash(khoa_can_bam)}\n")
    
    print("--- LẦN KHỞI ĐỘNG 2 (Khởi động lại server) ---")
    bang_2 = BamPhoQuat(m)
    print(f"Khóa {khoa_can_bam} rớt vào giỏ số: {bang_2.get_hash(khoa_can_bam)}\n")