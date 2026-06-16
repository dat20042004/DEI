def stable_insertion_sort_pairs(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # So sánh dựa trên phần tử đầu tiên của tuple (khóa)
        while j >= 0 and a[j][0] > key[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

pairs = [(2, 'a'), (1, 'b'), (2, 'c')]
print(stable_insertion_sort_pairs(pairs))
# Kết quả: [(1, 'b'), (2, 'a'), (2, 'c')] ((2,'a') vẫn đứng trước (2,'c'))