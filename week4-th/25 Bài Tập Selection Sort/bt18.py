# Giải thích lý thuyết:
# - Selection sort: Mỗi vòng lặp lớn chỉ swap tối đa 1 lần để đưa phần tử về đúng vị trí. Tổng số swap luôn <= n-1.
# - Bubble sort: Phải swap liên tục giữa hai phần tử kề nhau bất cứ khi nào sai thứ tự. Tổng số swap đúng bằng số cặp nghịch thế (inversions).
# Do đó, trên các mảng xáo trộn mạnh, Bubble sort tốn rất nhiều thao tác ghi (swap) dữ liệu so với Selection sort.

print("Selection sort tối ưu về số lượng ghi/swap dữ liệu hơn Bubble sort.")