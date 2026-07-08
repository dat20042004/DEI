def dem_doan_con(mang, k):
    dem = 0
    tong_hien_tai = 0
    bang_dem_tong = {0: 1} # Khởi tạo: tổng = 0 xuất hiện 1 lần
    
    for so in mang:
        tong_hien_tai += so
        # Nếu (Tổng hiện tại - k) đã từng xuất hiện, ta tìm được một đoạn con
        if (tong_hien_tai - k) in bang_dem_tong:
            dem += bang_dem_tong[tong_hien_tai - k]
            
        # Lưu lại tổng này vào bảng băm
        bang_dem_tong[tong_hien_tai] = bang_dem_tong.get(tong_hien_tai, 0) + 1
        
    return dem

print("Bài 12:", dem_doan_con([1, 1, 1], 2)) # 2 đoạn [cite: 147]