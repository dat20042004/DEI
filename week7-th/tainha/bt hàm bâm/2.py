class HashTableLinear:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        
    def put(self, key, value):
        idx = hash(key) % self.size
        # Nếu có người ở và không phải là key của mình thì đi tiếp
        while self.table[idx] is not None and self.table[idx][0] != key:
            idx = (idx + 1) % self.size # Thử ô kế tiếp [cite: 114]
            
        self.table[idx] = (key, value)

    def get(self, key):
        idx = hash(key) % self.size
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size
        return None