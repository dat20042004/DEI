# Bảng đối chiếu lý thuyết chi phí Insertion Sort:
#
# Trường hợp (Case)   | Số phép so sánh | Số lần dịch chuyển (Shift) | Độ phức tạp
# --------------------|-----------------|---------------------------|------------
# Best Case (Đã xếp)   | n - 1           | 0                         | O(n)
# Average Case (Ngẫu) | ~ n^2 / 4       | ~ n^2 / 4                 | O(n^2)
# Worst Case (Ngược)  | n(n-1) / 2      | n(n-1) / 2                | O(n^2)

def analyze_insertion_sort_cases():
    print("Insertion Sort có chi phí biến động mạnh dựa vào cấu trúc dữ liệu đầu vào.")
    print("Mảng đã sắp xếp đạt hiệu năng tuyến tính O(n), mảng ngược tốn chi phí cực đại O(n^2).")

analyze_insertion_sort_cases()