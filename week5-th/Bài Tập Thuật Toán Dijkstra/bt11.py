import heapq

def multi_source_dijkstra(adj, sources, n):
    dist = [float('inf')] * n
    pq = []
    
    # Nạp toàn bộ các đỉnh nguồn vào hàng đợi với khoảng cách ban đầu bằng 0
    for src in sources:
        dist[src] = 0
        heapq.heappush(pq, (0, src))
        
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    print("Khoảng cách ngắn nhất tới tập nguồn {0, 3}:", multi_source_dijkstra(graph, [0, 3], 6))