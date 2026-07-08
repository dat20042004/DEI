def hash_bang_phep_cong(tap_hop):
    tong_hash = 0
    for phan_tu in tap_hop:
        # Băm từng phần tử thành một số, rồi cộng dồn lại
        tong_hash += hash(phan_tu)
    return tong_hash

def hash_bang_phep_xor(tap_hop):
    ket_qua_xor = 0
    for phan_tu in tap_hop:
        # Dùng phép XOR (^) để trộn các bit lại với nhau
        ket_qua_xor ^= hash(phan_tu)
    return ket_qua_xor

# --- CHẠY THỬ NGHIỆM ---
if __name__ == "__main__":
    nhom_1 = [1, 2, 3]
    nhom_2 = [3, 1, 2] # Giống hệt nhóm 1, chỉ đảo thứ tự
    
    print("1. THỬ NGHIỆM VỚI TẬP HỢP BÌNH THƯỜNG (Set)")
    print(f"- Nhóm 1 {nhom_1} (Cộng): {hash_bang_phep_cong(nhom_1)}")
    print(f"- Nhóm 2 {nhom_2} (Cộng): {hash_bang_phep_cong(nhom_2)}")
    print("-> Kết quả phép Cộng khớp nhau hoàn toàn!\n")
    
    print(f"- Nhóm 1 {nhom_1} (XOR): {hash_bang_phep_xor(nhom_1)}")
    print(f"- Nhóm 2 {nhom_2} (XOR): {hash_bang_phep_xor(nhom_2)}")
    print("-> Kết quả phép XOR khớp nhau hoàn toàn!\n")
    
    print("-" * 50)
    print("2. THỬ NGHIỆM VỚI ĐA TẬP HỢP (Multiset - Cho phép phần tử trùng lặp)")
    # Giả sử có một nhóm chứa 2 số 1 giống nhau
    nhom_da_tap = [1, 1, 2]
    nhom_chỉ_co_2 = [2]
    
    print(f"- Nhóm {nhom_da_tap} (Cộng): {hash_bang_phep_cong(nhom_da_tap)}")
    print(f"- Nhóm {nhom_da_tap} (XOR) : {hash_bang_phep_xor(nhom_da_tap)}")
    print(f"- Nhóm {nhom_chỉ_co_2}      (XOR) : {hash_bang_phep_xor(nhom_chỉ_co_2)}")
    
    print("\n=> CẢNH BÁO QUAN TRỌNG VỀ XOR:")
    print("Nhóm [1, 1, 2] ra kết quả XOR giống hệt nhóm [2]. Vì hai số 1 khi XOR cho nhau sẽ triệt tiêu biến thành 0!")