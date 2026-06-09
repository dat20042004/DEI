def phan_tu_cuoi(a):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    return a[-1]

a = [4, 2, 7, 1, 3]
print(phan_tu_cuoi(a))