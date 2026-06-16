def count_shifts(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1  # Đếm mỗi lần dịch phần tử sang phải
            j -= 1
        a[j + 1] = key
    return shifts

print("Tổng số lần dịch chuyển:", count_shifts([3, 2, 1]))
# Kết quả: 3