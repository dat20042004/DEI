# Bài 9. Chuyển trung tố sang hậu tố (Thuật toán Shunting-Yard)
def infix_to_postfix(expression: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())
            stack.append(char)
            
    while stack:
        output.append(stack.pop())
        
    return "".join(output)

# Ví dụ kiểm thử
if __name__ == "__main__":
    print(infix_to_postfix("a+b*c"))  # Kết quả: 'abc*+'