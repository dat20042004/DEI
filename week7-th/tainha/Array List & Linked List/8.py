arr = [1, 2, 3, 4]
# Dùng List Comprehension là cách tối ưu và chuẩn Python nhất
arr = [x for x in arr if x % 2 != 0] # Xóa số chẵn
print("Sau khi xóa:", arr)