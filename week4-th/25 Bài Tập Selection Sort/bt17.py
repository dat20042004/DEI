def find_kth_smallest(a, k):
    n = len(a)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[k-1] # Phần tử nhỏ thứ k nằm tại chỉ số k-1

print(find_kth_smallest([7, 2, 5, 1, 9], 3))
# Kết quả: 5