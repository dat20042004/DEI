# Bài 4. Kiểm tra rỗng / đầy của hàng đợi có dung lượng cố định
class BoundedQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, x):
        if len(self.queue) >= self.capacity:
            print("Lỗi: Hàng đợi đầy (enqueue thất bại)")
            return False
        self.queue.append(x)
        return True

    def dequeue(self):
        if not self.queue:
            print("Lỗi: Hàng đợi rỗng (dequeue thất bại)")
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

# Ví dụ kiểm thử
if __name__ == "__main__":
    bq = BoundedQueue(2)
    bq.enqueue(1)
    bq.enqueue(2)
    bq.enqueue(3)  # Báo lỗi đầy
    print(f"Số lượng phần tử: {bq.count()}")
    bq.dequeue()
    bq.dequeue()
    bq.dequeue()  # Báo lỗi rỗng