# Bảng so sánh đặc tính thực tế giữa 3 thuật toán:
#
# Thuật toán      | Số phép so sánh (Ngẫu nhiên) | Ghi dữ liệu đặc trưng (Swap / Shift) | Ưu tiên dùng khi nào?
# ----------------|------------------------------|--------------------------------------|-----------------------------------------
# Bubble Sort     | Rất nhiều (O(n^2))           | Rất nhiều cặp Swap cục bộ (O(n^2))   | Ít dùng, chủ yếu để giảng dạy.
# Selection Sort  | Luôn cố định n(n-1)/2         | Rất ít, tối đa n-1 lần Swap          | Khi chi phí ghi đè lên bộ nhớ đắt đỏ.
# Insertion Sort  | Trung bình tốt (O(n^2))      | Dịch chuyển tuyến tính nhẹ (Shift)   | Khi mảng kích thước nhỏ hoặc gần như đã xếp.

def compare_algorithms():
    print("Trong nhóm O(n^2), Insertion Sort có hiệu năng chạy thực tế tốt nhất trên dữ liệu ngẫu nhiên.")

compare_algorithms()