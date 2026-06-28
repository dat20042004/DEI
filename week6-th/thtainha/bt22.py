# Bài 7. Đảo ngược hàng đợi
from collections import deque

def reverse_queue(q: deque) -> deque:
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    return q

# Ví dụ kiểm thử
if __name__ == "__main__":
    q = deque([1, 2, 3])
    print(list(reverse_queue(q)))  # Kết quả: [3, 2, 1]