def selection_sort_asc(a):
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print(selection_sort_asc([5, 2, 4, 6, 1, 3]))
# Kết quả: [1, 2, 3, 4, 5, 6]