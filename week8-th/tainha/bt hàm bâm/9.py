def two_sum(mang, target):
    da_thay = {} # Lưu {giá_trị_đã_thấy: vị_trí_của_nó}
    for i, so in enumerate(mang):
        phan_bu = target - so
        if phan_bu in da_thay:
            return (da_thay[phan_bu], i) # Trả về vị trí [cite: 137]
        da_thay[so] = i
    return None

print("Bài 9:", two_sum([2, 7, 11], 9)) # Kết quả: (0, 1)