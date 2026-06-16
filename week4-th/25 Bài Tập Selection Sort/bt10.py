def count_exact_swaps(a):
    n = len(a)
    exact_swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i: # Chỉ swap khi vị trí tìm được khác vị trí hiện tại
            a[i], a[min_idx] = a[min_idx], a[i]
            exact_swaps += 1
    return exact_swaps

print("Số swap thực sự:", count_exact_swaps([1, 2, 3])) # Kết quả: 0
print("Số swap thực sự:", count_exact_swaps([3, 2, 1])) # Kết quả: 1