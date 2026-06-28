# Bài 4. Phát hiện underflow / overflow
class BoundedStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []

    def push(self, x):
        if len(self.stack) >= self.capacity:
            print("Lỗi: overflow")
            return False
        self.stack.append(x)
        return True

    def pop(self):
        if not self.stack:
            print("Lỗi: underflow")
            return None
        return self.stack.pop()

# Ví dụ kiểm thử
if __name__ == "__main__":
    bs = BoundedStack(2)
    bs.push(1)
    bs.push(2)
    bs.push(3)  # Báo lỗi overflow
    bs.pop()
    bs.pop()
    bs.pop()  # Báo lỗi underflow