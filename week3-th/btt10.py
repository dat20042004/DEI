def dem_so_luot(a):
    so_luot = 0
    for i in range(len(a)):
        co_swap = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                co_swap = True
        so_luot += 1
        if not co_swap:
            break
    return so_luot

a = [2, 1, 3, 4]
print(dem_so_luot(a))