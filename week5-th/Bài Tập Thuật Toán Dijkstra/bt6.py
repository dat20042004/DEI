def dijkstra_early_stop(adj, s, t):
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    visited = [False] * n
    
    for _ in range(n):
        u = -1
        min_d = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
                
        if u == -1: break
        visited[u] = True
        
        # Dừng thuật toán sớm ngay khi lấy được đỉnh đích t ra khỏi tập chưa chốt
        if u == t:
            break
            
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    return dist[t]

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    print("Độ dài từ 0 tới 4 (Dừng sớm):", dijkstra_early_stop(graph, 0, 4))