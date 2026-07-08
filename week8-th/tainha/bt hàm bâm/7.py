
class HashTableRehash:
    def __init__(self, size=4):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(self.size)]
        
    def put(self, key, val):
        # Kiểm tra ngưỡng (Load factor > 0.75)
        if self.count / self.size > 0.75:
            self.rehash() # Gọi hàm mở rộng
            
        idx = hash(key) % self.size
        self.table[idx].append((key, val))
        self.count += 1
        
    def rehash(self):
        bang_cu = self.table
        self.size *= 2 # Nhân đôi kích thước mảng
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        
        # Băm lại toàn bộ dữ liệu cũ
        for gio in bang_cu:
            for k, v in gio:
                self.put(k, v)