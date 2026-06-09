def dem_swap(a):
    so_swap = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                so_swap += 1
    return so_swap

a = [3, 2, 1]
print(dem_swap(a))