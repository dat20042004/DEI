import heapq

def dijkstra_heap(adj, s):
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    
    # Hàng đợi ưu tiên chứa các cặp tuple dạng: (khoảng_cách, đỉnh_u)
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Nếu khoảng cách lấy ra lớn hơn khoảng cách tối ưu hiện tại thì bỏ qua
        if d > dist[u]:
            continue
            
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    print("Bản sử dụng Heap từ nguồn 0:", dijkstra_heap(graph, 0))