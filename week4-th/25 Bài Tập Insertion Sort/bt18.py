# Giải thích lý thuyết:
# - Dò từ phải sang trái (chuẩn): Ta so sánh ngay với phần tử lớn nhất của vùng đã sắp xếp. 
#   Nếu dữ liệu gần như đã sắp xếp, phép thử này thường trả về False lập tức -> mất O(1) kiểm tra.
# - Dò từ trái sang phải: Ta phải quét qua toàn bộ các phần tử nhỏ hơn ở đầu mảng trước khi tìm được điểm dừng, tốn nhiều phép so sánh vô ích.
print("Chiến lược dò từ phải sang trái giúp tối ưu hóa thời gian chạy thành O(n) cho mảng gần như đã sắp xếp.")