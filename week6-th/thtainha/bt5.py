# Bài 5. Duyệt và đếm phần tử (Không làm mất ngăn xếp gốc)
def count_and_print_stack(stack):
    temp_stack = []
    count = 0
    
    # Đọc phần tử theo thứ tự LIFO và chuyển sang ngăn xếp phụ
    elements = []
    while stack:
        val = stack.pop()
        elements.append(val)
        temp_stack.append(val)
        count += 1
        
    # In ra các phần tử theo thứ tự LIFO
    print("Các phần tử (thứ tự LIFO):", ", ".join(map(str, elements)))
    
    # Khôi phục lại ngăn xếp ban đầu
    while temp_stack:
        stack.append(temp_stack.pop())
        
    return count

# Ví dụ kiểm thử
if __name__ == "__main__":
    my_stack = [1, 2, 3]
    total = count_and_print_stack(my_stack)
    print(f"Số lượng phần tử: {total}")
    print(f"Ngăn xếp sau khôi phục: {my_stack}")