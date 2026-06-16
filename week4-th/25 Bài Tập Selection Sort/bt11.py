# Minh họa tính không ổn định của Selection Sort gốc
# Định dạng phần tử: (giá trị_khóa, nhãn)
a = [(2, 'a'), (2, 'b'), (1, 'c')]

# Bước 1: Tìm min trong đoạn [0, 3) -> tìm được (1, 'c') tại idx 2
# Bước 2: Hoán đổi a[0] và a[2] -> Mảng thành: [(1, 'c'), (2, 'b'), (2, 'a')]
# Thấy rằng (2, 'b') bây giờ đứng trước (2, 'a'), thứ tự ban đầu bị đảo lộn.

print("Minh họa lý thuyết: Bản chất hoán đổi từ xa phá vỡ tính ổn định.")