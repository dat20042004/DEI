def mot_luot(a):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

a = [5, 1, 4, 2, 8]
mot_luot(a)
print(a)