# Bài 12. Hình chữ nhật lớn nhất trong histogram
def largest_rectangle_area(heights) -> int:
    stack = []
    max_area = 0
    heights.append(0) # Thêm cột cao 0 vào cuối để dọn sạch stack khi kết thúc
    
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
        
    heights.pop() # Trả lại trạng thái cũ cho mảng dữ liệu đầu vào
    return max_area

# Ví dụ kiểm thử
if __name__ == "__main__":
    h = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle_area(h))  # Kết quả: 10