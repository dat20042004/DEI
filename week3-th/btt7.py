def sort_ky_tu(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

a = ['d', 'a', 'c', 'b']
sort_ky_tu(a)
print(a)