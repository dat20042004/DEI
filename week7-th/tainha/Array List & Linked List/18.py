class Node:
    def __init__(self, val=0, next=None):
        self.val = val   # Lưu trữ giá trị
        self.next = next # Trỏ tới nút tiếp theo

def tim_kiem(head, val):
    vi_tri = 0
    curr = head
    while curr:
        if curr.val == val:
            return vi_tri
        curr = curr.next
        vi_tri += 1
    return -1

if __name__ == "__main__":
    node1 = Node(1, Node(2, Node(3))) # Cách viết gộp tạo nhanh danh sách 1 -> 2 -> 3
    print("Vị trí của số 2 là:", tim_kiem(node1, 2))