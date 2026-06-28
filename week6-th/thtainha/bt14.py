# Bài 14. Bài toán nhịp giá cổ phiếu (Stock Span)
def calculate_span(prices):
    n = len(prices)
    span = [0] * n
    stack = [] # Lưu cặp (chỉ số, giá trị)
    
    for i in range(n):
        days = 1
        while stack and stack[-1][1] <= prices[i]:
            days += stack.pop()[0]
        stack.append((days, prices[i]))
        span[i] = days
        
    return span

# Ví dụ kiểm thử
if __name__ == "__main__":
    prices = [100, 80, 60, 70, 60, 75, 85]
    print(calculate_span(prices))  # Kết quả: [1, 1, 1, 2, 1, 4, 6]