# Bài 5. Tìm front và rear mà không làm xóa các phần tử
def peek_front_rear(queue_list):
    if not queue_list:
        return None, None
    front = queue_list[0]
    rear = queue_list[-1]
    return front, rear

# Ví dụ kiểm thử
if __name__ == "__main__":
    queue = [4, 5, 6]
    f, r = peek_front_rear(queue)
    print(f"front={f}, rear={r}")  # Kết quả: front=4, rear=6