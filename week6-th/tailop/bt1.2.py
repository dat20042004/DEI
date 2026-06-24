from collections import deque       

# Khởi tạo ngăn xếp rỗng
myStack = deque()

# Thêm phần tử vào ngăn xếp (push)
myStack.append('data science')
myStack.append('data analytics')

print("Stack sau khi thêm 2 phần tử:", myStack)

# Thêm tiếp các phần tử khác
myStack.append('data structures and algorithms')
myStack.append('learning data analytics')
myStack.append('big data')

print("Stack sau khi thêm nhiều phần tử:", myStack)

# Lấy phần tử ra khỏi ngăn xếp (pop)
myStack.pop()   # lấy 'big data'
myStack.pop()   # lấy 'learning data analytics'

# Xem ngăn xếp cuối cùng
print("Stack sau khi pop 2 lần:", myStack)
