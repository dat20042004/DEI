# Bài 15. Sắp xếp một ngăn xếp (Lớn nhất ở đỉnh khi kết thúc)
def sort_stack(stack):
    aux_stack = []
    
    while stack:
        # Lấy phần tử hiện tại ra khỏi ngăn xếp gốc
        tmp = stack.pop()
        
        # Nếu ngăn xếp phụ không rỗng và đỉnh ngăn xếp phụ nhỏ hơn tmp
        while aux_stack and aux_stack[-1] < tmp:
            stack.append(aux_stack.pop())
            
        aux_stack.append(tmp)
        
    # Đưa các phần tử từ ngăn xếp phụ ngược trở lại ngăn xếp ban đầu
    while aux_stack:
        stack.append(aux_stack.pop())
        
    return stack

# Ví dụ kiểm thử
if __name__ == "__main__":
    s = [3, 1, 2]
    print(sort_stack(s))  # Kết quả: [3, 2, 1] (Phần tử 1 ở đỉnh của ngăn xếp)