def insertion_sort_print(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"Bước {i}: {a}")

insertion_sort_print([3, 1, 2])
# Kết quả:
# Bước 1: [1, 3, 2]
# Bước 2: [1, 2, 3]