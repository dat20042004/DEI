# Khi mọi phần tử cách vị trí đúng tối đa k bước, vòng lặp `while` bên trong chạy không quá k lần.
# Tổng thời gian xử lý toàn mảng là O(n * k).
def insertion_sort_k_bounded(a, k):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        step_count = 0
        while j >= 0 and a[j] > key and step_count <= k:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
            step_count += 1
        a[j + 1] = key
    return a, shifts

# Đoạn mảng có độ lệch vị trí cực đại k = 2
arr, total_shifts = insertion_sort_k_bounded([3, 1, 2, 5, 4, 7, 6], 2)
print("Mảng đã xếp:", arr, "| Tổng số shift:", total_shifts)