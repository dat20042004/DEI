def duyet_mang(arr):
    for x in arr:
        yield x # Biến hàm thành một generator (dạng cơ bản của Iterator)

for phan_tu in duyet_mang([1, 2, 3]):
    print("Duyệt:", phan_tu)