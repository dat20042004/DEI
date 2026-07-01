import sys
arr = []
# Python tự động quản lý sức chứa (capacity). 
# Dù đôi khi tốn thời gian chép mảng, trung bình mỗi lần append vẫn là O(1)
for i in range(5):
    arr.append(i)
    print(f"Số lượng: {len(arr)} | Kích thước byte: {sys.getsizeof(arr)}")