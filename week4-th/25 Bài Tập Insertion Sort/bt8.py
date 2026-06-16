def insertion_sort_k_steps(a, k):
    # Thực hiện k vòng chèn đầu tiên (i chạy từ 1 đến k)
    for i in range(1, min(k + 1, len(a))):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print(insertion_sort_k_steps([4, 3, 2, 1], k=1))
# Kết quả: [3, 4, 2, 1]