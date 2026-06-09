def so_luot_toi_thieu(a):
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
    return so_luot - 1  # trừ lượt kiểm tra cuối không có swap

a = [1, 2, 3, 5, 4]
print(so_luot_toi_thieu(a))