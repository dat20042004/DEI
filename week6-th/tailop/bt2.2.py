from collections import deque 

# Khởi tạo hàng đợi rỗng
q = deque()

# Thêm phần tử vào hàng đợi (enqueue)
q.append('data analytics')
q.append('data science')
q.append('AI fundamentals')

# Thêm tiếp các phần tử khác
q.append('data structures and algorithms')
q.append('big data')
q.append('learning data analytics')

# In hàng đợi hiện tại
print("Queue ban đầu:", q)

# Lấy phần tử ra khỏi hàng đợi (dequeue)
print("Dequeue:", q.popleft())   # lấy 'data analytics'
print("Dequeue:", q.popleft())   # lấy 'data science'

# In hàng đợi sau khi dequeue
print("Queue sau khi lấy 2 phần tử:", q)
