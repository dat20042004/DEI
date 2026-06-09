def do_lech_k(a, k):
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

# Mảng gần sắp xếp, k=2
a = [1, 3, 2, 4, 6, 5, 7, 8]
print("So luot:", do_lech_k(a, 2))