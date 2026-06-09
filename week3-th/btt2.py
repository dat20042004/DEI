def bubble_sort_tang(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

a = [5, 1, 4, 2, 8]
bubble_sort_tang(a)
print(a)