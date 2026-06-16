def binary_insertion_sort(a):
    comparisons = 0
    for i in range(1, len(a)):
        key = a[i]
        
        # Tìm kiếm nhị phân vị trí chèn trong đoạn a[0..i-1]
        low, high = 0, i - 1
        while low <= high:
            comparisons += 1
            mid = (low + high) // 2
            if key < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        # Vị trí chèn đúng là `low`, tiến hành dịch chuyển
        for j in range(i - 1, low - 1, -1):
            a[j + 1] = a[j]
        a[low] = key
    return a, comparisons

arr, comp = binary_insertion_sort([4, 2, 7, 1, 3])
print("Mảng đã xếp:", arr, "| Số lần so sánh nhị phân:", comp)