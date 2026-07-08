import random

# --- CÁCH 1: TÍNH JACCARD TRỰC TIẾP (Cách truyền thống, cực kỳ chậm nếu dữ liệu lớn) ---
def jaccard_that(tap_A, tap_B):
    phan_giao = len(tap_A.intersection(tap_B))
    phan_hop = len(tap_A.union(tap_B))
    return phan_giao / phan_hop

# --- CÁCH 2: TÍNH JACCARD BẰNG MINHASH (Cách hiện đại, siêu nhanh cho Big Data) ---
class MinHash:
    def __init__(self, k_ham_bam):
        self.k = k_ham_bam
        # Tạo ra k cái "chìa khóa" ngẫu nhiên. Mỗi chìa khóa đại diện cho 1 hàm băm.
        self.chia_khoa = [random.randint(1, 99999) for _ in range(self.k)]

    def tao_chu_ky(self, tap_hop):
        chu_ky = []
        
        # Chạy qua từng hàm băm
        for khoa in self.chia_khoa:
            min_hash_cua_tap = float('inf') # Khởi tạo giá trị ban đầu là vô cực lớn
            
            # Băm mọi phần tử trong tập hợp
            for phan_tu in tap_hop:
                # Trộn phần tử với "chìa khóa" để tạo hàm băm
                gia_tri_bam = hash((phan_tu, khoa))
                
                # CHỈ LƯU LẠI GIÁ TRỊ NHỎ NHẤT (MinHash)
                if gia_tri_bam < min_hash_cua_tap:
                    min_hash_cua_tap = gia_tri_bam
                    
            chu_ky.append(min_hash_cua_tap)
            
        return chu_ky # Chữ ký lúc này chỉ là một mảng có đúng k con số

    def uoc_luong_jaccard(self, chu_ky_a, chu_ky_b):
        # Chỉ cần đếm xem hai chữ ký giống nhau bao nhiêu lần ở cùng một vị trí
        so_lan_khop = 0
        for i in range(self.k):
            if chu_ky_a[i] == chu_ky_b[i]:
                so_lan_khop += 1
                
        # Trả về tỷ lệ giống nhau
        return so_lan_khop / self.k

# --- CHẠY THỬ NGHIỆM ---
if __name__ == "__main__":
    # Giả sử ta có 2 văn bản (tập hợp các từ) rất giống nhau
    # Tập A có từ 1 đến 1000. Tập B có từ 200 đến 1200.
    tap_hop_A = set([f"tu_khoa_{i}" for i in range(1, 1000)])
    tap_hop_B = set([f"tu_khoa_{i}" for i in range(200, 1200)])
    
    print("1. KẾT QUẢ TÍNH TOÁN TRỰC TIẾP CHÍNH XÁC:")
    ket_qua_that = jaccard_that(tap_hop_A, tap_hop_B)
    print(f"-> Độ tương đồng là: {ket_qua_that * 100:.2f}%\n")
    
    print("2. KẾT QUẢ ƯỚC LƯỢNG BẰNG MINHASH (Chữ ký 100 con số):")
    # Khởi tạo MinHash với 100 hàm băm
    mh = MinHash(k_ham_bam=100)
    
    # Ép 2 tập hợp lớn thành 2 chữ ký siêu ngắn
    chu_ky_A = mh.tao_chu_ky(tap_hop_A)
    chu_ky_B = mh.tao_chu_ky(tap_hop_B)
    
    # Ước lượng
    ket_qua_uoc_luong = mh.uoc_luong_jaccard(chu_ky_A, chu_ky_B)
    print(f"-> Độ tương đồng ước lượng: {ket_qua_uoc_luong * 100:.2f}%")
    print(f"-> So với kết quả thật, chỉ sai số cực kỳ nhỏ, nhưng tiết kiệm được vô số bộ nhớ!")