# Giải thích & kiểm chứng:
# Cặp nghịch thế là cặp chỉ số (i, j) mà i < j nhưng a[i] > a[j].
# Mỗi lần vòng lặp dịch chuyển một phần tử lớn hơn ra sau, ta đã triệt tiêu chính xác 1 cặp nghịch thế.

def count_inversions_by_shift(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return shifts

print("Số nghịch thế (bằng số shift):", count_inversions_by_shift([2, 4, 1, 3]))
# Kết quả: 3 (Các cặp nghịch thế: (2,1), (4,1), (4,3))