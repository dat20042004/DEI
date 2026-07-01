# Bài 10. Hàng đợi ưu tiên cơ bản (Min-Priority Queue dạng chèn giữ thứ tự giảm dần để pop phần tử nhỏ nhất)
class SimplePriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        # Chèn cặp phần tử (độ ưu tiên, giá trị định danh) vào mảng
        self.queue.append((priority, item))
        # Sắp xếp mảng giảm dần theo độ ưu tiên để phần tử ưu tiên nhỏ nhất nằm ở cuối hàng đợi
        self.queue.sort(key=lambda x: x[0], reverse=True)

    def pop(self):
        if not self.queue:
            return None
        return self.queue.pop()[1] # Trả về giá trị của item có mức ưu tiên nhỏ nhất đầu tiên

# Ví dụ kiểm thử
if __name__ == "__main__":
    pq = SimplePriorityQueue()
    pq.push("Task A", 3)
    pq.push("Task B", 1)
    pq.push("Task C", 2)
    print(pq.pop())  # Kết quả phần tử có độ ưu tiên cao nhất (nhỏ nhất): Task B