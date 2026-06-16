def count_swaps(a):
    n = len(a)
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        swaps += 1 # Đếm hoán đổi cơ bản theo thuật toán chuẩn
    return swaps

print("Số lần swap:", count_swaps([3, 2, 1]))
