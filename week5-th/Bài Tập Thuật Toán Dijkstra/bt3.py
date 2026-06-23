def dijkstra_v2(adj, s):
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    visited = [False] * n
    
    for _ in range(n):
        u = -1
        min_d = float('inf')
        # Tìm đỉnh u chưa chốt có khoảng cách nhỏ nhất
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
                
        if u == -1: break
        visited[u] = True
        
        # Nới lỏng cạnh
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    return dist

if __name__ == "__main__":
    # Đồ thị G1
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    print("Khoảng cách từ s=0:", dijkstra_v2(graph, 0))