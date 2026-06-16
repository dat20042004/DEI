# Giải thích sự liên hệ:
# - Cả Selection Sort và Heap Sort đều chia mảng thành 2 phần: phần đã sắp xếp và phần chưa sắp xếp.
# - Selection Sort quét tuần tự tuyến tính mất O(n) để tìm phần tử lớn/nhỏ nhất trong vùng chưa sắp xếp.
# - Heap Sort tổ chức vùng chưa sắp xếp dưới dạng cây nhị phân (Heap), rút ngắn thời gian tìm và lấy phần tử lớn/nhỏ nhất xuống chỉ còn O(log n).
# Nhờ vậy, tổng thời gian giảm từ O(n^2) xuống O(n log n).
print("Heap sort chính là phiên bản cải tiến cấu trúc dữ liệu của Selection sort.")