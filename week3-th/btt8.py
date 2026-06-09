def kiem_tra_k_luot(a, k):
    for i in range(k):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            return False
    return True

a = [3, 2, 1]
k = 1
print(kiem_tra_k_luot(a, k))