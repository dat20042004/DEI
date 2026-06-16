def selection_sort_abs(a):
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if abs(a[j]) < abs(a[min_idx]):
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print(selection_sort_abs([-3, 1, -2, 2]))
# Kết quả: [1, -2, 2, -3] (hoặc [1, 2, -2, -3] tùy thuộc vào thứ tự ban đầu)