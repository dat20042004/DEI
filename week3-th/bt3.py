def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Vòng lặp j chạy tịnh tiến từ 0 đến n-i-1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                # Đổi chỗ 2 phần tử
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]
print('Mang chua duoc sap xep la:', arr)

bubble_sort(arr)
print('Mang duoc sap xep la:    ', arr)