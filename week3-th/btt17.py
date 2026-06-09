def k_lon_nhat(a, k):
    for i in range(k):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [3, 1, 4, 1, 5]
k = 2
print(k_lon_nhat(a, k))