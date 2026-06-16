# Đánh giá sử dụng:
# 1. Partial Selection Sort: Độ phức tạp O(n * k). Tốt nhất khi k rất nhỏ (ví dụ k = 1, 2, 3) vì thuật toán cài đặt cực kỳ đơn giản, không tốn chi phí xây dựng cấu trúc dữ liệu mới.
# 2. Heap Method: Độ phức tạp O(n + k log n) sử dụng Min-Heap. Tốt nhất khi k lớn đáng kể so với n vì chi phí trích xuất log n tối ưu hơn quét tuyến tính tuyến tính nhiều lần.
print("Chọn Partial Selection khi k rất nhỏ; chọn Heap khi k lớn.")