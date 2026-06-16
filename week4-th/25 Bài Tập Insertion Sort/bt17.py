# Thực nghiệm: Trên mảng gần như đã xếp, số lần dịch chuyển tiệm cận O(1) mỗi vòng.
# Do đó tổng thời gian xử lý mảng tiệm cận tuyến tính O(n).
def check_nearly_sorted():
    a = [1, 2, 4, 3, 5]
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    print(f"Mảng sau sắp xếp: {a}, Tổng số shift: {shifts}")

check_nearly_sorted()  # Kết quả shift: 1