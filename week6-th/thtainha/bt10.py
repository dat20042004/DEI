# Bài 10. Cài đặt ngăn xếp bằng hai hàng đợi
from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # Thao tác push chi phí O(n) để tối ưu thao tác pop thành O(1)
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if not self.q1:
            return None
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0] if self.q1 else None

    def isEmpty(self) -> bool:
        return len(self.q1) == 0

# Ví dụ kiểm thử
if __name__ == "__main__":
    s = StackUsingQueues()
    s.push(1)
    s.push(2)
    print(s.pop())  # Kết quả: 2