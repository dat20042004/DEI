# Bài 1. Cài đặt hàng đợi cơ bản dựa trên nguyên tắc FIFO
from collections import deque

class BasicQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.popleft()

    def front(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

# Ví dụ kiểm thử
if __name__ == "__main__":
    q = BasicQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Kết quả: 1