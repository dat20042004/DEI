arr = [1, 2, 3, 4, 5]
k = 2
k = k % len(arr)
# Cắt mảng và ghép lại
arr_xoay = arr[-k:] + arr[:-k] 
print("Xoay k vị trí:", arr_xoay)