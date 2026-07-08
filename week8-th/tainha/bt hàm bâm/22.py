def ham_bam_cap(a, b):
    # Bước 1: Tính mã băm riêng lẻ cho từng thành phần
    hash_a = hash(a)
    hash_b = hash(b)
    
    # Bước 2: Chọn một hằng số C
    # Trong các hệ thống lớn (như thư viện Boost của C++), họ hay dùng số ma thuật 0x9e3779b9
    # Ở đây ta dùng một số nguyên tố đơn giản là 31 cho dễ hiểu
    C = 31 
    
    # Bước 3: Áp dụng công thức hash_combine
    # Lấy hash_a nhân với hằng số C, sau đó XOR (^) với hash_b
    hash_ket_hop = (hash_a * C) ^ hash_b
    
    return hash_ket_hop

if __name__ == "__main__":
    # Thử nghiệm với 2 cặp số giống y hệt nhau nhưng bị đảo ngược vị trí
    cap_1 = (1, 2)
    cap_2 = (2, 1)
    
    ket_qua_1 = ham_bam_cap(cap_1[0], cap_1[1])
    ket_qua_2 = ham_bam_cap(cap_2[0], cap_2[1])
    
    print(f"Mã băm của cặp {cap_1} là: {ket_qua_1}")
    print(f"Mã băm của cặp {cap_2} là: {ket_qua_2}")
    
    print("-" * 40)
    if ket_qua_1 != ket_qua_2:
        print("-> TUYỆT VỜI! Cặp (1, 2) và (2, 1) đã ra hai mã số hoàn toàn khác nhau.")
        print("-> Sự phân biệt này giúp Bảng băm không bị va chạm.")