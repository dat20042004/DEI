# Bài 1. Cài đặt ngăn xếp bằng mảng
class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

# Ví dụ kiểm thử
if __name__ == "__main__":
    s = StackArray()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # Kết quả: 3