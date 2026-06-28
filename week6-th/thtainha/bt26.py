# Bài 11. Giá trị lớn nhất trong cửa sổ trượt dùng deque đơn điệu
from collections import deque

def max_sliding_window(nums, k):
    q = deque() # Lưu trữ index của phần tử
    result = []
    
    for i, num in enumerate(nums):
        # Loại bỏ các index nằm ngoài phạm vi cửa sổ hiện tại
        if q and q[0] < i - k + 1:
            q.popleft()
            
        # Duy trì deque đơn điệu giảm dần bằng cách loại bỏ phần tử nhỏ hơn giá trị hiện tại
        while q and nums[q[-1]] < num:
            q.pop()
            
        q.append(i)
        
        # Thêm giá trị lớn nhất của cửa sổ hiện tại vào kết quả
        if i >= k - 1:
            result.append(nums[q[0]])
            
    return result

# Ví dụ kiểm thử
if __name__ == "__main__":
    a = [1, 3, -1, -3, 5, 3]
    k = 3
    print(max_sliding_window(a, k))  # Kết quả: [3, 3, 5, 5]