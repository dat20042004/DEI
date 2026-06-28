# Bài 11. Phần tử lớn hơn kế tiếp (Next Greater Element)
def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = [] # Lưu trữ các chỉ mục (index) của mảng
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
        
    return result

# Ví dụ kiểm thử
if __name__ == "__main__":
    a = [2, 1, 3]
    print(next_greater_element(a))  # Kết quả: [3, 3, -1]