import heapq

def minimax_dijkstra(adj, s, t):
    n = len(adj)
    # dist[v] lưu trọng số của cạnh lớn nhất có thể xuất hiện trên đường đi từ s đến v sao cho giá trị này nhỏ nhất
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, w in adj[u]:
            # Phép relax tùy chỉnh: bottleneck mới là max của đường đi cũ và cạnh (u, v)
            current_bottleneck = max(dist[u], w)
            if current_bottleneck < dist[v]:
                dist[v] = current_bottleneck
                heapq.heappush(pq, (dist[v], v))
                
    return dist[t]

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    print("Trọng số cạnh lớn nhất nhỏ nhất trên đường 0->4 là:", minimax_dijkstra(graph, 0, 4))