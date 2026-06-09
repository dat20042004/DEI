def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Phải reset lại swapped = False ở mỗi lượt vòng lặp i
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        # Đặt ngoài vòng lặp j: Nếu đi hết 1 lượt j mà không có cặp nào đổi chỗ -> mảng đã xong
        if not swapped:
            return

arr = [60, 32, 15, 12, 52, 71, 90, -1, -10, -30, -155, 75]
bubble_sort(arr)

print('Mang duoc sap xep la:')
for i in range(len(arr)):
    print("%d" % arr[i], end=" ") # Hoặc dùng: print(arr[i], end=" ")