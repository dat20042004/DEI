def sort_on_dinh(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]

a = [(2, 'a'), (1, 'b'), (2, 'c')]
sort_on_dinh(a)
print(a)