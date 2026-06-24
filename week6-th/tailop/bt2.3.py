from queue import Queue 

# Khởi tạo hàng đợi với kích thước tối đa là 5
q = Queue(maxsize=5) 

# Kiểm tra kích thước ban đầu
print("Kích thước ban đầu:", q.qsize()) 

# Thêm phần tử vào hàng đợi (enqueue)
q.put('data analytics')                                         
q.put('data structures and algorithms') 
q.put('big data') 
q.put('learning data analytics') 

# Kiểm tra kích thước sau khi thêm
print("Kích thước sau khi thêm:", q.qsize())                                                    

# Lấy phần tử ra khỏi hàng đợi (dequeue)
print("Dequeue:", q.get())   # lấy 'data analytics'
print("Dequeue:", q.get())   # lấy 'data structures and algorithms'

# Kiểm tra kích thước còn lại
print("Kích thước sau khi lấy 2 phần tử:", q.qsize())
