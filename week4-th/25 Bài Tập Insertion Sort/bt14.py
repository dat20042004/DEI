def insertion_sort_multi_keys(students):
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1
        while j >= 0:
            # Điều kiện 1: Điểm của a[j] thấp hơn key -> cần dịch chuyển ra sau
            # Điều kiện 2: Điểm bằng nhau, nhưng tên của a[j] lớn hơn key (theo từ điển) -> dịch ra sau
            if (students[j][1] < key[1]) or (students[j][1] == key[1] and students[j][0] > key[0]):
                students[j + 1] = students[j]
                j -= 1
            else:
                break
        students[j + 1] = key
    return students

data = [('An', 8), ('Ba', 9), ('Cu', 8)]
print(insertion_sort_multi_keys(data))
# Kết quả: [('Ba', 9), ('An', 8), ('Cu', 8)]