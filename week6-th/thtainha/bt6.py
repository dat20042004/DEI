# Bài 6. Dấu ngoặc cân bằng
def is_balanced(s: str) -> bool:
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
            
    return len(stack) == 0

# Ví dụ kiểm thử
if __name__ == "__main__":
    print(is_balanced("([]{})"))  # Kết quả: True
    print(is_balanced("([)]"))    # Kết quả: False