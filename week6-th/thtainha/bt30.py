# Bài 15. Mô phỏng bộ lập lịch Round-Robin và tính thời điểm hoàn thành (Completion Time)
from collections import deque

def round_robin_scheduling(processes, burst_times, quantum):
    # processes: danh sách tên tiến trình ví dụ ['P1', 'P2', 'P3']
    # burst_times: thời gian xử lý tương ứng ví dụ [5, 2, 4]
    
    queue = deque()
    # Khởi tạo hàng đợi chứa cặp thông tin (tên tiến trình, thời gian còn lại)
    for p, b in zip(processes, burst_times):
        queue.append([p, b])
        
    current_time = 0
    completion_time = {}
    
    while queue:
        p, remaining_time = queue.popleft()
        
        if remaining_time <= quantum:
            current_time += remaining_time
            completion_time[p] = current_time
        else:
            current_time += quantum
            queue.append([p, remaining_time - quantum])
            
    return completion_time

# Ví dụ kiểm thử
if __name__ == "__main__":
    procs = ['P1', 'P2', 'P3']
    bursts = [5, 2, 4]
    q_size = 2
    print(round_robin_scheduling(procs, bursts, q_size))
    # Kết quả: {'P2': 4, 'P3': 10, 'P1': 11}