class BangBamChaining:
    def __init__(self, kich_thuoc=5):
        self.kich_thuoc = kich_thuoc
        # Tạo mảng gồm các danh sách (giỏ) rỗng
        self.bang = [[] for _ in range(kich_thuoc)] 

    def put(self, key, value):
        idx = hash(key) % self.kich_thuoc
        # Cập nhật nếu đã có key
        for i, (k, v) in enumerate(self.bang[idx]):
            if k == key:
                self.bang[idx][i] = (key, value)
                return
        # Thêm mới nếu chưa có
        self.bang[idx].append((key, value))

    def remove(self, key):
        idx = hash(key) % self.kich_thuoc
        # Tìm và xóa khỏi danh sách phụ
        for i, (k, v) in enumerate(self.bang[idx]):
            if k == key:
                del self.bang[idx][i] # Xóa trực tiếp rất đơn giản
                print(f"Đã xóa khóa '{key}'")
                return True
        return False
    
class BangBamOpenAddressing:
    def __init__(self, kich_thuoc=5):
        self.kich_thuoc = kich_thuoc
        self.bang = [None] * kich_thuoc
        self.DA_XOA = "TOMBSTONE" # Nhãn đánh dấu đã xóa

    def put(self, key, value):
        idx = hash(key) % self.kich_thuoc
        buoc_di = 0
        
        # Tìm ô trống hoặc ô đã bị dán nhãn xóa
        while self.bang[idx] is not None and self.bang[idx] != self.DA_XOA:
            if self.bang[idx][0] == key: # Nếu key đã tồn tại thì ghi đè
                self.bang[idx] = (key, value)
                return
            idx = (idx + 1) % self.kich_thuoc
            buoc_di += 1
            if buoc_di >= self.kich_thuoc:
                print("Bảng đã đầy!")
                return
                
        self.bang[idx] = (key, value)

    def remove(self, key):
        idx = hash(key) % self.kich_thuoc
        buoc_di = 0
        
        # Đi tìm phần tử cần xóa
        while self.bang[idx] is not None:
            if self.bang[idx] != self.DA_XOA and self.bang[idx][0] == key:
                self.bang[idx] = self.DA_XOA # Dán nhãn thay vì làm trống
                print(f"Đã dán nhãn xóa cho khóa '{key}'")
                return True
            
            idx = (idx + 1) % self.kich_thuoc
            buoc_di += 1
            if buoc_di >= self.kich_thuoc: # Đã đi hết một vòng
                break
        return False
