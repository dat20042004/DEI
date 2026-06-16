def insertion_sort_abs(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # Sử dụng nghiêm ngặt dấu '>' để giữ tính ổn định cho các phần tử bằng trị tuyệt đối
        while j >= 0 and abs(a[j]) > abs(key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print(insertion_sort_abs([-3, 1, -2, 2]))
# Kết quả: [1, -2, 2, -3]