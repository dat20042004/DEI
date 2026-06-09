def sort_do_dai(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if len(a[j]) > len(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

a = ['abc', 'a', 'ab']
sort_do_dai(a)
print(a)