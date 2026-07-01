# Bài 13. Chứng minh hàng đợi cấu tạo từ 2 Stack có chi phí Amortized O(1)
# Dưới đây là phân tích logic mã nguồn theo phương pháp kế toán (Accounting Method)

class AmortizedQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x: int) -> None:
        # Chi phí thực tế là 1 đơn vị bước tính toán.
        # Chúng ta tính hóa đơn giá 3 đơn vị tiền xu (tokens):
        # - 1 đồng trả tiền cho chính thao tác chèn vào in_stack.
        # - 1 đồng dự trữ trả cho thao tác pop khỏi in_stack trong tương lai.
        # - 1 đồng dự trữ trả cho thao tác push vào out_stack trong tương lai.
        self.in_stack.append(x)

    def dequeue(self) -> int:
        # Nếu out_stack còn phần tử, thao tác pop tốn 1 đơn vị thực tế (lấy từ số dư tích lũy).
        if not self.out_stack:
            # Nếu out_stack rỗng, ta chuyển toàn bộ dữ liệu từ in_stack sang.
            # Mỗi vòng lặp chuyển 1 phần tử này đã được trả trước hoàn toàn bằng 2 đồng xu tích lũy khi enqueue.
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        if not self.out_stack:
            return None
        return self.out_stack.pop()

# Vì vậy, chi phí trung bình (amortized) của mọi hành động luôn là O(1) hằng số.# Bài 13. Chứng minh hàng đợi cấu tạo từ 2 Stack có chi phí Amortized O(1)
# Dưới đây là phân tích logic mã nguồn theo phương pháp kế toán (Accounting Method)

class AmortizedQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x: int) -> None:
        # Chi phí thực tế là 1 đơn vị bước tính toán.
        # Chúng ta tính hóa đơn giá 3 đơn vị tiền xu (tokens):
        # - 1 đồng trả tiền cho chính thao tác chèn vào in_stack.
        # - 1 đồng dự trữ trả cho thao tác pop khỏi in_stack trong tương lai.
        # - 1 đồng dự trữ trả cho thao tác push vào out_stack trong tương lai.
        self.in_stack.append(x)

    def dequeue(self) -> int:
        # Nếu out_stack còn phần tử, thao tác pop tốn 1 đơn vị thực tế (lấy từ số dư tích lũy).
        if not self.out_stack:
            # Nếu out_stack rỗng, ta chuyển toàn bộ dữ liệu từ in_stack sang.
            # Mỗi vòng lặp chuyển 1 phần tử này đã được trả trước hoàn toàn bằng 2 đồng xu tích lũy khi enqueue.
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        if not self.out_stack:
            return None
        return self.out_stack.pop()

# Vì vậy, chi phí trung bình (amortized) của mọi hành động luôn là O(1) hằng số.