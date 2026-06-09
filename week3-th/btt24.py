def xac_dinh_so_luot(ban_dau, sau):
    a = ban_dau[:]
    for luot in range(len(a)):
        if a == sau:
            return luot
        for j in range(len(a) - 1 - luot):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return -1

ban_dau = [4, 3, 2, 1]
sau = [3, 2, 1, 4]
print(xac_dinh_so_luot(ban_dau, sau))