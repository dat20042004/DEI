class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_selection_sort(head):
    if not head: return None
    
    dummy = Node(0)
    tail = dummy
    
    while head:
        # Tìm nút có giá trị nhỏ nhất và nút đứng trước nó
        min_prev = None
        min_node = head
        
        prev = head
        curr = head.next
        while curr:
            if curr.data < min_node.data:
                min_node = curr
                min_prev = prev
            prev = curr
            curr = curr.next
            
        # Tách nút nhỏ nhất ra khỏi danh sách cũ
        if min_node == head:
            head = head.next
        else:
            min_prev.next = min_node.next
            
        # Nối nút nhỏ nhất vào danh sách kết quả mới
        tail.next = min_node
        tail = min_node
        tail.next = None
        
    return dummy.next

# Chạy thử nghiệm
h = Node(3); h.next = Node(1); h.next.next = Node(2)
sorted_h = linked_list_selection_sort(h)
res = []
while sorted_h:
    res.append(sorted_h.data)
    sorted_h = sorted_h.next
print(res) # Kết quả: [1, 2, 3]