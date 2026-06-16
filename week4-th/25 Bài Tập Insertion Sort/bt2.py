def insertion_sort_asc(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print(insertion_sort_asc([5, 2, 4, 6, 1, 3]))
# Kết quả: [1, 2, 3, 4, 5, 6]