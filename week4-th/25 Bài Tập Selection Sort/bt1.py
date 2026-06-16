def move_min_to_front(a):
    if not a: return a
    min_idx = 0
    for j in range(1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    a[0], a[min_idx] = a[min_idx], a[0]
    return a

print(move_min_to_front([4, 2, 7, 1, 3])) 
