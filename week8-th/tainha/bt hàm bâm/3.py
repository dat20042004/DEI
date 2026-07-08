def dem_tan_suat(mang):
    dem = {} # Khởi tạo bảng băm (dict)
    for phan_tu in mang:
        if phan_tu in dem:
            dem[phan_tu] += 1
        else:
            dem[phan_tu] = 1
    return dem

print("Bài 3:", dem_tan_suat(['a', 'b', 'a', 'c', 'a'])) # {'a':3, 'b':1, 'c':1} [cite: 117]