# Bài 8. Tính biểu thức hậu tố (RPN)
def eval_RPN(expression: str) -> int:
    stack = []
    # Phân tách theo khoảng trắng nếu có, hoặc duyệt từng ký tự nếu viết liền
    tokens = expression.split() if " " in expression else list(expression)
    
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+": stack.append(a + b)
            elif token == "-": stack.append(a - b)
            elif token == "*": stack.append(a * b)
            elif token == "/": stack.append(int(a / b)) # Chia lấy phần nguyên
        else:
            stack.append(int(token))
            
    return stack[0]

# Ví dụ kiểm thử
if __name__ == "__main__":
    print(eval_RPN("3 4 + 2 *"))  # (3+4)*2 = 14