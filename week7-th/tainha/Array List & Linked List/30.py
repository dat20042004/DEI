# --- ĐOẠN CODE CƠ SỞ (LUÔN ĐỂ Ở ĐẦU FILE) ---
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def in_danh_sach(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
# ---------------------------------------------


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # Trong Python, dict thông thường lưu được thứ tự

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        
        # Nếu đầy, xóa phần tử đầu tiên (cũ nhất)
        if len(self.cache) > self.cap:
            cu_nhat = next(iter(self.cache))
            self.cache.pop(cu_nhat)
            
    def get(self, key):
        if key not in self.cache:
            return -1
        # Lấy ra và nhét lại vào cuối để làm "mới nhất"
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

if __name__ == "__main__":
    cache = LRUCache(2) # Sức chứa = 2
    cache.put(1, "A")
    cache.put(2, "B")
    print("Lấy key 1:", cache.get(1)) # Đẩy A lên mới nhất
    cache.put(3, "C") # Vượt sức chứa, xóa B (vì B cũ nhất)
    print("Lấy key 2:", cache.get(2)) # Kết quả: -1 (đã bị xóa)