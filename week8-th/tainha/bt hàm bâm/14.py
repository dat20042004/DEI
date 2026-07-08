class LazyDeleteHash:
    def __init__(self):
        self.table = [None] * 10
        self.DELETED = "DA_XOA" # Nhãn đánh dấu [cite: 154]
        
    def xoa(self, key):
        idx = hash(key) % 10
        while self.table[idx] is not None:
            if self.table[idx] == key:
                self.table[idx] = self.DELETED # Đánh dấu đã xóa thay vì làm trống
                return
            idx = (idx + 1) % 10