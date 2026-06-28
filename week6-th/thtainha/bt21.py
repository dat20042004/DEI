# Bài 6. Cài đặt hàng đợi bằng hai ngăn xếp
class QueueWithStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x: int) -> None:
        self.in_stack.append(x)

    def dequeue(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None
        return self.out_stack.pop()

# Ví dụ kiểm thử
if __name__ == "__main__":
    qw = QueueWithStacks()
    qw.enqueue(1)
    qw.enqueue(2)
    print(qw.dequeue())  # Kết quả: 1