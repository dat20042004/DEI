class MyHashSet:
    def __init__(self):
        # Tạo mảng lớn, mỗi ô chứa 1 list rỗng
        self.table = [[] for _ in range(100)] 
        
    def add(self, key):
        idx = key % 100
        if key not in self.table[idx]: # Đảm bảo không trùng lặp
            self.table[idx].append(key)
            
    def contains(self, key):
        return key in self.table[key % 100]

# Chạy thử
s = MyHashSet()
s.add(1); s.add(1); s.add(2)
print("Bài 11 - Set có số 1 không?:", s.contains(1)) # True