def gnome_sort(a):
    idx = 0
    n = len(a)
    while idx < n:
        if idx == 0 or a[idx] >= a[idx - 1]:
            idx += 1
        else:
            a[idx], a[idx - 1] = a[idx - 1], a[idx]
            idx -= 1  # Di chuyển lùi lại để kiểm tra phần tử vừa swap
    return a

print(gnome_sort([3, 2, 1]))
# Kết quả: [1, 2, 3]