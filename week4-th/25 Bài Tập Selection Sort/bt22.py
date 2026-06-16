# Phân tích đánh đổi:
# Để Selection Sort vừa ổn định (stable) vừa chạy trực tiếp trên mảng hiện tại không tốn bộ nhớ phụ (in-place),
# ta buộc phải thay thế thao tác Swap (hoán đổi từ xa) bằng thao tác Shift (dịch chuyển cả một dãy phần tử phía sau).
# Việc dịch chuyển phần tử mất chi phí O(n) cho mỗi vòng, làm tăng số thao tác ghi vào bộ nhớ đáng kể.
print("Đổi tính ổn định lấy việc tăng số thao tác dịch chuyển dữ liệu.")