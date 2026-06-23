import heapq

def dijkstra_k_stops(adj, s, t, max_edges):
    n = len(adj)
    # Trạng thái mở rộng bao gồm: dist[u][số_cạnh_đã_sử_dụng]
    dist = [[float('inf')] * (max_edges + 1) for _ in range(n)]
    
    dist[s][0] = 0
    pq = [(0, s, 0)] # (chi phí, đỉnh, số cạnh đã đi qua)
    
    while pq:
        cost, u, edges_used = heapq.heappop(pq)
        if cost > dist[u][edges_used]: continue
        if u == t: return cost
        
        # Nếu số lượng cạnh đã sử dụng chạm ngưỡng giới hạn k cho phép thì không đi tiếp nữa
        if edges_used < max_edges:
            for v, w in adj[u]:
                if cost + w < dist[v][edges_used + 1]:
                    dist[v][edges_used + 1] = cost + w
                    heapq.heappush(pq, (cost + w, v, edges_used + 1))
                    
    min_cost = min(dist[t])
    return min_cost if min_cost != float('inf') else -1

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    # Tìm đường từ 0 sang 4 đi qua tối đa k=2 cạnh
    print("Chi phí đi tối đa qua 2 cạnh từ 0->4 là:", dijkstra_k_stops(graph, 0, 4, 2))