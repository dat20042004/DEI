class BloomFilter:
    def __init__(self, kich_thuoc_m, so_ham_bam_k):
        """
        m: Số lượng bit (công tắc) trong mảng.
        k: Số lượng hàm băm (số công tắc cần bật cho mỗi phần tử).
        """
        self.m = kich_thuoc_m
        self.k = so_ham_bam_k
        self.bit_array = [0] * self.m  # Khởi tạo mảng toàn số 0
        
    def _tinh_cac_vi_tri_bam(self, item):
        # Hàm nội bộ: Băm 1 phần tử ra k vị trí khác nhau
        vi_tri_cac_cong_tac = []
        for i in range(self.k):
            # Mẹo để tạo ra k hàm băm: Nối thêm số i vào cuối chuỗi trước khi băm
            chuoi_da_tron = f"{item}_hambam_{i}"
            vi_tri = hash(chuoi_da_tron) % self.m
            vi_tri_cac_cong_tac.append(vi_tri)
        return vi_tri_cac_cong_tac

    def add(self, item):
        # Băm phần tử ra k vị trí và bật các công tắc đó lên số 1
        cac_vi_tri = self._tinh_cac_vi_tri_bam(item)
        for vt in cac_vi_tri:
            self.bit_array[vt] = 1
            
    def contains(self, item):
        # Kiểm tra xem toàn bộ k công tắc của phần tử này có đang bật (1) không
        cac_vi_tri = self._tinh_cac_vi_tri_bam(item)
        for vt in cac_vi_tri:
            if self.bit_array[vt] == 0:
                # Chỉ cần thấy 1 công tắc tắt (0), khẳng định 100% KHÔNG TỒN TẠI
                return False
                
        # Nếu tất cả đều là 1 -> CÓ THỂ tồn tại (chấp nhận rủi ro dương tính giả)
        return True

# --- CHẠY THỬ NGHIỆM ---
if __name__ == "__main__":
    # Tạo Bloom Filter với 20 công tắc và 3 hàm băm
    bf = BloomFilter(kich_thuoc_m=20, so_ham_bam_k=3)
    
    # 1. Thêm dữ liệu thật
    bf.add("apple")
    bf.add("banana")
    
    print(f"Trạng thái mảng bit: {bf.bit_array}\n")
    
    # 2. Kiểm tra phần tử chắc chắn có
    print(f"Có 'apple' không? -> {bf.contains('apple')}")     # True
    
    # 3. Kiểm tra phần tử CHẮC CHẮN KHÔNG CÓ
    print(f"Có 'cat' không? -> {bf.contains('cat')}")         # False
    
    # 4. CHỨNG MINH DƯƠNG TÍNH GIẢ (Báo CÓ nhầm)
    # Ta nhồi nhét quá nhiều phần tử vào một mảng quá nhỏ để ép nó nhận nhầm
    bf_nho = BloomFilter(kich_thuoc_m=5, so_ham_bam_k=3)
    bf_nho.add("dog")
    bf_nho.add("fox")
    bf_nho.add("ant")
    
    print(f"\nMảng bit bị nhồi nhét: {bf_nho.bit_array}")
    # Mặc dù ta chưa hề add "elephant", nhưng vô tình các công tắc của nó đã bị dog, fox, ant bật lên giùm!
    print(f"Có 'elephant' không? -> {bf_nho.contains('elephant')} (ĐÂY LÀ DƯƠNG TÍNH GIẢ!)")