def sort_hoc_sinh(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j][1] < a[j+1][1]:
                a[j], a[j+1] = a[j+1], a[j]
            elif a[j][1] == a[j+1][1] and a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]

a = [('An', 8), ('Ba', 9), ('Cu', 8)]
sort_hoc_sinh(a)
print(a)