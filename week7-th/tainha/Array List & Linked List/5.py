arr = [1, 2, 3, 4]
dem_chan = 0
for so in arr:
    print("Phần tử:", so)
    if so % 2 == 0:
        dem_chan += 1
print("Tổng số chẵn:", dem_chan)