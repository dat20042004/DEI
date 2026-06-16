def sort_students(students):
    n = len(students)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if students[j][1] < students[min_idx][1]: # So sánh theo điểm số
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]
    return students

print(sort_students([('An', 8), ('Ba', 5)]))
# Kết quả: [('Ba', 5), ('An', 8)]