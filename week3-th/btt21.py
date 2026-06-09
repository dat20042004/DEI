def sort_on_dinh_2(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]

a = [(2, 'x'), (1, 'a'), (2, 'b'), (1, 'z')]
sort_on_dinh_2(a)
print("Bubble sort (on dinh):", a)

# So sánh với selection sort (không ổn định)
b = [(2, 'x'), (1, 'a'), (2, 'b'), (1, 'z')]
for i in range(len(b)):
    min_i = i
    for j in range(i+1, len(b)):
        if b[j][0] < b[min_i][0]:
            min_i = j
    b[i], b[min_i] = b[min_i], b[i]
print("Selection sort (co the khong on dinh):", b)