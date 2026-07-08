def day_lien_tiep(mang):
    tap_hop = set(mang)
    max_dai = 0
    
    for so in tap_hop:
        # Nếu số đứng trước nó không có, đây là điểm bắt đầu của 1 dãy mới
        if so - 1 not in tap_hop: 
            so_hien_tai = so
            do_dai = 1
            
            while so_hien_tai + 1 in tap_hop: # Đếm lên liên tục
                so_hien_tai += 1
                do_dai += 1
                
            max_dai = max(max_dai, do_dai)
            
    return max_dai

print("Bài 13:", day_lien_tiep([100, 4, 200, 1, 3, 2])) # Kết quả: 4 (do có dãy 1,2,3,4) [cite: 150]