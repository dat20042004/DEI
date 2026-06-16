# Thực hành 03.4: Thuật toán sắp xếp chọn - mảng kiểu string

arr = ["Banana", "Apple", "Orange", "Mango", "Grapes"]

n = len(arr)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        # So sánh theo thứ tự từ điển
        if arr[j] < arr[min_index]:
            min_index = j
    
    # Đổi chỗ phần tử nhỏ nhất tìm được với phần tử vị trí i
    min_value = arr.pop(min_index)
    arr.insert(i, min_value)

print("Sorted array:", arr)