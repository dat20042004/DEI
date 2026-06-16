def shell_sort(a):
    n = len(a)
    gap = n // 2  # Sử dụng dãy gap gốc của Shell
    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            j = i
            while j >= gap and a[j - gap] > key:
                a[j] = a[j - gap]
                j -= gap
            a[j] = key
        gap //= 2
    return a

print(shell_sort([8, 3, 5, 1, 4, 2, 7, 6]))
# Kết quả: [1, 2, 3, 4, 5, 6, 7, 8]