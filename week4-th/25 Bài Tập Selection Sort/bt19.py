# Phân tích kỹ thuật:
# - Số vòng lặp: Giảm đi một nửa (chỉ cần chạy n/2 vòng).
# - Số phép so sánh: Vẫn giữ nguyên cấu trúc toán học O(n^2).
# - Trường hợp biên quan trọng: Khi phần tử cực đại (max) nằm ngay tại vị trí 'left'. Sau khi swap đưa 'min' về vị trí 'left', giá trị cực đại lúc này đã bị dịch chuyển sang vị trí cũ của 'min' (min_idx). Nếu không cập nhật lại `max_idx = min_idx`, thuật toán sẽ swap sai giá trị cực đại.
print("Đã xử lý trường hợp biên tại Bài 9.")