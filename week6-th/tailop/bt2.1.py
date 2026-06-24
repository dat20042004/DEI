# Thực hành 2.1: Hàng đợi (Queue) bằng list
myQueue = []

# Thêm phần tử vào hàng đợi (enqueue)
myQueue.append('data science')
myQueue.append('data analytics')

# Thêm tiếp các phần tử khác
myQueue.append('data structures and algorithms')
myQueue.append('big data')
myQueue.append('learning data analytics')

# In hàng đợi hiện tại
print("Queue ban đầu:", myQueue)

# Lấy phần tử ra khỏi hàng đợi (dequeue)
print("Dequeue:", myQueue.pop(0))   # lấy 'data science'
print("Dequeue:", myQueue.pop(0))   # lấy 'data analytics'

# In hàng đợi sau khi dequeue
print("Queue sau khi lấy 2 phần tử:", myQueue)
