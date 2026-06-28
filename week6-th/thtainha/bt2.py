# Bài 2. Đảo ngược chuỗi dùng ngăn xếp
def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

# Ví dụ kiểm thử
if __name__ == "__main__":
    print(reverse_string("abc"))  # Kết quả: 'cba'