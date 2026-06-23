import heapq

def count_shortest_paths(adj, s):
    n = len(adj)
    dist = [float('inf')] * n
    paths_count = [0] * n
    
    dist[s] = 0
    paths_count[s] = 1
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, w in adj[u]:
            # Tìm thấy đường đi mới có chi phí ngắn hơn
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                paths_count[v] = paths_count[u]
                heapq.heappush(pq, (dist[v], v))
            # Tìm thấy một đường đi khác có chi phí bằng với chi phí tối ưu cũ
            elif dist[u] + w == dist[v]:
                paths_count[v] += paths_count[u]
                
    return dist, paths_count

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    dists, counts = count_shortest_paths(graph, 0)
    print("Số lượng đường đi ngắn nhất đến từng đỉnh:", counts)