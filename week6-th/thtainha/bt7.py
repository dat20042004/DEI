# Bài 7. Min Stack getMin O(1)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

# Ví dụ kiểm thử
if __name__ == "__main__":
    ms = MinStack()
    ms.push(5)
    ms.push(3)
    ms.push(7)
    print(ms.getMin())  # Kết quả: 3