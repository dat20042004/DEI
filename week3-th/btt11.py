def sort_tri_tuyet_doi(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if abs(a[j]) > abs(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

a = [-3, 1, -2, 2]
sort_tri_tuyet_doi(a)
print(a)