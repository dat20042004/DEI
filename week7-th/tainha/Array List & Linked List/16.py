class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def push_front(head, val):
    return Node(val, head) # Thêm đầu

def push_back(head, val):
    if not head: return Node(val)
    curr = head
    while curr.next: # Chạy đến cuối
        curr = curr.next
    curr.next = Node(val) # Thêm cuối
    return head