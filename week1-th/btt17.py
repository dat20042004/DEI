''' Bài 17. Tìm kiếm có lính canh (Sentinel)
Cài đặt tìm kiếm tuyến tính theo kỹ thuật lính canh: tạm đặt giá trị x vào cuối mảng làm
“lính canh”, nhờ đó vòng lặp chắc chắn dừng và bỏ bớt một điều kiện kiểm tra biên (i < n)
trong mỗi vòng. Hãy so sánh số phép so sánh với cách thông thường.'''
def sentinel_search(a, x):
    a.append(x)  # Đặt x làm "lính canh" ở cuối mảng 
    i = 0
    
    while a[i] != x:  # Chỉ cần kiểm tra xem đã gặp x chưa, không sợ lố mảng 
        i = i + 1
        
    a.pop()  # Tìm xong thì xóa con lính canh đi để trả lại mảng nguyên bản cho người ta
    
    # Nếu vị trí dừng lại nhỏ hơn độ dài mảng ban đầu thì đó là hàng thật
    if i < len(a):
        return i
    return -1