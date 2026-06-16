def insertion_sort_desc(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:  # Đổi dấu so sánh
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print(insertion_sort_desc([5, 2, 4, 6, 1]))
# Kết quả: [6, 5, 4, 2, 1]