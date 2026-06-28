# Bài 2. Hàng đợi vòng (Circular Queue)
class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, x: int) -> bool:
        if self.isFull():
            print("Hàng đợi đầy")
            return False
        self.queue[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self) -> int:
        if self.isEmpty():
            print("Hàng đợi rỗng")
            return None
        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Ví dụ kiểm thử
if __name__ == "__main__":
    cq = CircularQueue(4)
    cq.enqueue(10)
    cq.enqueue(20)
    print(cq.dequeue())  # Kết quả: 10