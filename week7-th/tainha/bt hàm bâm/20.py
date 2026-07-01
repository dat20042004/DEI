def so_sanh_phan_bo(tap_khoa, m):
    # Tạo danh sách để đếm số lượng phần tử rơi vào mỗi giỏ (bucket)
    dem_bucket = [0] * m 
    
    # Băm từng khóa và tăng biến đếm của giỏ tương ứng lên 1
    for khoa in tap_khoa:
        idx = khoa % m
        dem_bucket[idx] += 1
        
    # Tính số lượng giỏ bị bỏ trống
    so_gio_trong = dem_bucket.count(0)
    
    # Tính giỏ bị quá tải nặng nhất (chứa nhiều phần tử nhất)
    max_va_cham = max(dem_bucket)
    
    return dem_bucket, so_gio_trong, max_va_cham

if __name__ == "__main__":
    # Tạo một tập dữ liệu có quy luật: các số cách nhau 4 đơn vị 
    # Ví dụ: 0, 4, 8, 12, 16, 20, 24... đến 196 (tổng cộng 50 số)
    tap_du_lieu_co_quy_luat = [i * 4 for i in range(50)]
    
    # THỰC NGHIỆM 1: m = 16 (Lũy thừa của 2)
    m1 = 16
    phan_bo_16, gio_trong_16, max_16 = so_sanh_phan_bo(tap_du_lieu_co_quy_luat, m1)
    
    print("THỰC NGHIỆM 1: Bảng có kích thước m = 16 (Lũy thừa của 2: 2^4)")
    print(f"- Chi tiết từng giỏ: {phan_bo_16}")
    print(f"- Số giỏ bị bỏ trống: {gio_trong_16} giỏ (Quá lãng phí bộ nhớ!)")
    print(f"- Giỏ kẹt xe nhất chứa: {max_16} phần tử (Va chạm rất nặng)")
    print("-" * 50)
    
    # THỰC NGHIỆM 2: m = 17 (Số nguyên tố)
    m2 = 17
    phan_bo_17, gio_trong_17, max_17 = so_sanh_phan_bo(tap_du_lieu_co_quy_luat, m2)
    
    print("THỰC NGHIỆM 2: Bảng có kích thước m = 17 (Số nguyên tố)")
    print(f"- Chi tiết từng giỏ: {phan_bo_17}")
    print(f"- Số giỏ bị bỏ trống: {gio_trong_17} giỏ (Tận dụng tốt không gian)")
    print(f"- Giỏ kẹt xe nhất chứa: {max_17} phần tử (Dữ liệu rải rất đều)")