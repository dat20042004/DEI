def count_comparisons(a):
    n = len(a)
    comparisons = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return comparisons

print("Mảng ngẫu nhiên:", count_comparisons([5, 3, 1, 4, 2])) # n = 5 -> 10
print("Mảng đã sắp xếp:", count_comparisons([1, 2, 3, 4, 5])) # n = 5 -> 10