def double_selection_sort(a):
    n = len(a)
    comparisons = 0
    left = 0
    right = n - 1
    
    while left < right:
        min_idx = left
        max_idx = left
        for j in range(left + 1, right + 1):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
            elif a[j] > a[max_idx]:
                max_idx = j
                
        # Hoán đổi phần tử nhỏ nhất về vị trí left
        a[left], a[min_idx] = a[min_idx], a[left]
        
        # Nếu max_idx trùng với left, vị trí của max đã bị đổi sang min_idx
        if max_idx == left:
            max_idx = min_idx
            
        # Hoán đổi phần tử lớn nhất về vị trí right
        a[right], a[max_idx] = a[max_idx], a[right]
        
        left += 1
        right -= 1
    return a, comparisons

arr, total_comp = double_selection_sort([5, 1, 4, 2, 8])
print("Mảng sau sắp xếp:", arr)
print("Số lần so sánh:", total_comp)