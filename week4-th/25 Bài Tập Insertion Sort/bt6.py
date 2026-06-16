def count_comparisons(a):
    comparisons = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1  # Tính phép so sánh a[j] > key sắp diễn ra
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return comparisons

print("Best case [1, 2, 3]:", count_comparisons([1, 2, 3]))    # Kết quả: 2
print("Worst case [3, 2, 1]:", count_comparisons([3, 2, 1]))  # Kết quả: 3