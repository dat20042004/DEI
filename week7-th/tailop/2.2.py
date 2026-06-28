class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def delete_node(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head
    currentNode.next = currentNode.next.next
    return head

node1 = Node('AI')
node2 = Node('ML')
node3 = Node('DL')
node4 = Node('IT')
node5 = Node('Blockchain')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before del:")
search(node1)
# Delete node4
node1 = delete_node(node1, node4)
print("\nAfter del:")
search(node1)
