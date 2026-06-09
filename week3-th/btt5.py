def dem_so_sanh(a):
    so_ss = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            so_ss += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return so_ss

a = [1, 2, 3]
print(dem_so_sanh(a))