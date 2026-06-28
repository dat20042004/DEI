# Bài 8. Hàng đợi hai đầu (Deque) sử dụng mảng/list động
class CustomDeque:
    def __init__(self):
        self.items = []

    def pushFront(self, x):
        self.items.insert(0, x)

    def pushBack(self, x):
        self.items.append(x)

    def popFront(self):
        return self.items.pop(0) if self.items else None

    def popBack(self):
        return self.items.pop() if self.items else None

    def display(self):
        return self.items

# Ví dụ kiểm thử
if __name__ == "__main__":
    dq = CustomDeque()
    dq.pushFront(1)
    dq.pushBack(2)
    print(dq.display())  # Kết quả: [1, 2]