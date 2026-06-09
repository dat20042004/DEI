def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        if not swapped:
            return

# Mảng dữ liệu mẫu
arr = [60, 32, 15, 12, 52, 71, 90, -1, -10, -30, -155, 75]
bubble_sort_descending(arr)

print('Mang duoc sap xep tu lon den be la:')
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")