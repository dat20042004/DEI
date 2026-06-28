# Bài 3. Mô phỏng dãy thao tác trên Queue
from collections import deque

def simulate_queue_operations(operations):
    queue = deque()
    for op in operations:
        if op.startswith("enq"):
            _, val = op.split()
            queue.append(int(val))
        elif op == "deq":
            if queue:
                print(f"deq in {queue.popleft()}")
            else:
                print("deq lỗi: Queue rỗng")
    print(f"Trạng thái cuối cùng: {list(queue)}")

# Ví dụ kiểm thử
if __name__ == "__main__":
    ops = ["enq 5", "enq 7", "deq"]
    simulate_queue_operations(ops)  # In: deq in 5 -> Trạng thái cuối cùng: [7]