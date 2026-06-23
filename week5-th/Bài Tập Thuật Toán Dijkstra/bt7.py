def dijkstra_trace_path(adj, s, t):
    n = len(adj)
    dist = [float('inf')] * n
    parent = [-1] * n
    visited = [False] * n
    
    dist[s] = 0
    for _ in range(n):
        u = -1
        min_d = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1 or u == t: break
        visited[u] = True
        
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u # Lưu lại đỉnh trước
                
    # Truy vết ngược từ t về s
    if dist[t] == float('inf'):
        return [], float('inf')
        
    path = []
    curr = t
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    
    return path, dist[t]

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    path, length = dijkstra_trace_path(graph, 0, 4)
    print(f"Đường đi: {' -> '.join(map(str, path))} (Độ dài: {length})")