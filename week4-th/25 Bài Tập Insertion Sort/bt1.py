def insert_into_sorted(a, x):
    a.append(x)
    i = len(a) - 2
    while i >= 0 and a[i] > x:
        a[i + 1] = a[i]
        i -= 1
    a[i + 1] = x
    return a

print(insert_into_sorted([1, 3, 5, 7], 4))
# Kết quả: [1, 3, 4, 5, 7]