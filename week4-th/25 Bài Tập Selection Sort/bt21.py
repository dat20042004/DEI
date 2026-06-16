# Chứng minh toán học:
# Trong thuật toán Selection sort chuẩn, vòng lặp ngoài chạy từ i = 0 đến n-2.
# Với mỗi giá trị i, vòng lặp trong luôn thực hiện so sánh với j chạy từ i+1 đến n-1.
# Số lần chạy của vòng trong ứng với mỗi i là: (n - 1 - i).
# Tổng số phép so sánh S = (n-1) + (n-2) + ... + 2 + 1 = n * (n - 1) / 2.
# Công thức này hoàn toàn phụ thuộc vào kích thước mảng n, không phụ thuộc vào giá trị các phần tử bên trong mảng.
print("Chứng minh: Số phép so sánh luôn luôn là n(n-1)/2 bất kể mảng đầu vào.")