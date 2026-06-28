# Bài 14. Đếm số hit trong cửa sổ thời gian T giây gần nhất dùng hàng đợi
from collections import deque

class TimeWindowHitCounter:
    def __init__(self, time_window: int = 300):
        self.queue = deque()
        self.time_window = time_window

    def record_hit(self, timestamp: int):
        self.queue.append(timestamp)
        self._clean_expired(timestamp)

    def get_hits(self, current_time: int) -> int:
        self._clean_expired(current_time)
        return len(self.queue)

    def _clean_expired(self, current_time: int):
        # Loại bỏ các hit đã quá hạn nằm ngoài phạm vi cửa sổ thời gian
        while self.queue and self.queue[0] <= current_time - self.time_window:
            self.queue.popleft()

# Ví dụ kiểm thử
if __name__ == "__main__":
    counter = TimeWindowHitCounter(300) # Đếm hit trong 300 giây qua
    counter.record_hit(10)
    counter.record_hit(20)
    counter.record_hit(310) # Hit này khiến hit tại giây thứ 10 bị hết hạn
    print(counter.get_hits(315))  # Kết quả: 2 (chỉ còn hit tại giây 20 và 310)