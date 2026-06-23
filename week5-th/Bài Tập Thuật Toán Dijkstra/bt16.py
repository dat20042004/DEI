import heapq

def dijkstra_node_weights(adj_edges, node_costs, s, t):
    # Kỹ thuật: Khởi tạo khoảng cách xuất phát bằng chính chi phí của đỉnh nguồn s
    n = len(node_costs)
    dist = [float('inf')] * n
    dist[s] = node_costs[s]
    
    pq = [(node_costs[s], s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v in adj_edges[u]:
            # Cộng thêm chi phí đi vào đỉnh v thay vì cộng chi phí của cạnh
            if dist[u] + node_costs[v] < dist[v]:
                dist[v] = dist[u] + node_costs[v]
                heapq.heappush(pq, (dist[v], v))
                
    return dist[t]

if __name__ == "__main__":
    # Định nghĩa cấu trúc đồ thị không trọng số ở cạnh
    simple_adj = [[1, 2], [3], [1, 3, 4], [4, 5], [5], []]
    costs_on_nodes = [2, 4, 1, 5, 3, 2] # Trọng số của từng đỉnh từ 0 đến 5
    print("Chi phí đi từ 0 đến 4 dựa trên trọng số đỉnh:", dijkstra_node_weights(simple_adj, costs_on_nodes, 0, 4))