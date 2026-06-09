def dem_nghich_the(a):
    dem = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                dem += 1
    return dem

def dem_swap_bubble(a):
    so_swap = 0
    b = a[:]
    for i in range(len(b)):
        for j in range(len(b) - 1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                so_swap += 1
    return so_swap

a = [2, 3, 1]
print("Nghich the:", dem_nghich_the(a))
print("So swap:", dem_swap_bubble(a))