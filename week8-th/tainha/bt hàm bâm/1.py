class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        # Tạo mảng gồm các list rỗng
        self.table = [[] for _ in range(size)] 
        
    def get_hash(self, key):
        return hash(key) % self.size # Tính xem nằm ở giỏ nào
        
    def put(self, key, value):
        idx = self.get_hash(key)
        # Kiểm tra xem key đã có chưa để cập nhật
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx][i] = (key, value)
                return
        # Nếu chưa có thì thêm vào giỏ
        self.table[idx].append((key, value))
        
    def get(self, key):
        idx = self.get_hash(key)
        for kv in self.table[idx]:
            if kv[0] == key:
                return kv[1] # Trả về giá trị
        return None

# Chạy thử
ht = HashTableChaining()
ht.put('a', 1)
print("Bài 1:", ht.get('a')) # Kết quả: 1 [cite: 111]