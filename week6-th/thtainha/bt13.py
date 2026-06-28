# Bài 13. DFS dùng ngăn xếp tường minh (khử đệ quy)
def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Thêm các đỉnh kề chưa duyệt vào ngăn xếp (đảo ngược để duyệt đúng thứ tự ưu tiên)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return result

# Ví dụ kiểm thử
if __name__ == "__main__":
    # Đồ thị biểu diễn dưới dạng danh sách kề
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': [], 'F': []
    }
    print(dfs_iterative(graph, 'A'))  # Kết quả: ['A', 'B', 'D', 'E', 'C', 'F']