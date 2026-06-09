def bubble_sort_toi_uu(a):
    so_luot = 0
    for i in range(len(a)):
        co_swap = False
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                co_swap = True
        so_luot += 1
        if not co_swap:
            break
    return so_luot

a = [1, 2, 3, 4]
print(bubble_sort_toi_uu(a))