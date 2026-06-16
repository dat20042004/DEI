def stable_selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        
        # Thay vì swap, ta dịch các phần tử để chèn min_value vào vị trí i
        min_value = a[min_idx]
        for k in range(min_idx, i, -1):
            a[k] = a[k-1]
        a[i] = min_value
    return a

# Test tính ổn định với các cặp (khóa, nhãn)
pairs = [(2, 'a'), (2, 'b'), (1, 'c')]
print(stable_selection_sort(pairs))
# Kết quả duy trì đúng thứ tự: [(1, 'c'), (2, 'a'), (2, 'b')]