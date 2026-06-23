def count_nodes_within_radius(adj, s, max_d):
    # Sử dụng kết quả khoảng cách từ hàm Dijkstra đã có
    from math import inf
    n = len(adj)
    dist = [inf] * n
    dist[s] = 0
    visited = [False] * n
    
    for _ in range(n):
        u = -1
        min_d = inf
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1: break
        visited[u] = True
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    # Đếm số đỉnh thỏa mãn điều kiện dist[i] <= max_d
    count = sum(1 for d in dist if d <= max_d)
    return count

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    print("Số đỉnh có khoảng cách <= 3 là:", count_nodes_within_radius(graph, 0, 3))