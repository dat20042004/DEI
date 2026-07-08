# Cài đặt hàm băm đa thức (Polynomial Rolling Hash)
def ham_bam_da_thuc(chuoi, p=31, m=1000000009):
    gia_tri_hash = 0
    
    # Duyệt qua từng chữ cái
    for ky_tu in chuoi:
        ma_ascii = ord(ky_tu)
        # Lấy giá trị cũ nhân với p, cộng thêm chữ cái mới, rồi chia lấy dư cho m
        gia_tri_hash = (gia_tri_hash * p + ma_ascii) % m
        
    return gia_tri_hash

if __name__ == "__main__":
    # Bài 2 bị lỗi 'abc' và 'cba' giống nhau, giờ ta thử lại xem sao nhé:
    hash_abc = ham_bam_da_thuc("abc")
    hash_cba = ham_bam_da_thuc("cba")
    
    print(f"Mã băm của 'abc': {hash_abc}")
    print(f"Mã băm của 'cba': {hash_cba}")
    
    if hash_abc != hash_cba:
        print("-> Tuyệt vời! 'abc' và 'cba' đã ra hai con số hoàn toàn khác nhau.")