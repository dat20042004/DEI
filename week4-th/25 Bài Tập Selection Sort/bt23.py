# Bảng phân tích hiệu năng:
# Loại đầu vào   |  Số phép so sánh  |  Số phép Swap (Bản chuẩn)
# ---------------|-------------------|-------------------------
# Đã sắp xếp     |     n(n-1)/2      |          n-1
# Ngẫu nhiên     |     n(n-1)/2      |          n-1
# Ngược hoàn toàn|     n(n-1)/2      |          n-1
#
# Nhận xét: Dù mảng có trạng thái nào thì cấu trúc 2 vòng lặp lồng nhau cố định của Selection Sort vẫn quét O(n^2) phép so sánh.
print("Độ phức tạp thời gian luôn là O(n^2) trong mọi trường hợp.")