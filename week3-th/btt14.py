def cocktail_sort(a):
    trai = 0
    phai = len(a) - 1
    while trai < phai:
        for j in range(trai, phai):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        phai -= 1
        for j in range(phai, trai, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
        trai += 1

a = [5, 1, 4, 2, 8]
cocktail_sort(a)
print(a)