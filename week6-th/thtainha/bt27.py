# Bài 12. Bài toán Josephus dùng hàng đợi mô phỏng
from collections import deque

def josephus_survivor(n: int, k: int) -> int:
    queue = deque(range(1, n + 1))
    
    while len(queue) > 1:
        # Chuyển k-1 phần tử đầu xuống cuối hàng đợi
        for _ in range(k - 1):
            queue.append(queue.popleft())
        # Loại bỏ người thứ k ra khỏi vòng tròn
        queue.popleft()
        
    return queue[0]

# Ví dụ kiểm thử
if __name__ == "__main__":
    print(josephus_survivor(5, 2))  # Kết quả: 3