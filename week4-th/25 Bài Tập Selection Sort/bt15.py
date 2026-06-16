def partial_selection_sort(a, k):
    n = len(a)
    # Chỉ chạy đúng k vòng lặp ngoài cùng
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print(partial_selection_sort([5, 3, 1, 4, 2], 2))
# Kết quả: [1, 2, 5, 4, 3] (2 phần tử đầu tiên đã được định vị chính xác)