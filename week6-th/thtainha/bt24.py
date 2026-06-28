# Bài 9. BFS dùng hàng đợi duyệt theo tầng
from collections import deque

def bfs_traversal(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Ví dụ kiểm thử
if __name__ == "__main__":
    # Đồ thị dạng danh sách kề
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': [], 'F': []
    }
    print(bfs_traversal(graph, 'A'))  # Thứ tự theo tầng: ['A', 'B', 'C', 'D', 'E', 'F']