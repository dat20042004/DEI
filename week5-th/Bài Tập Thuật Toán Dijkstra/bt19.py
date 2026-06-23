import heapq

def max_probability_path(adj, s, t):
    n = len(adj)
    # dist[v] lưu xác suất thành công lớn nhất từ s tới v
    dist = [0.0] * n
    dist[s] = 1.0
    
    # Heap ưu tiên lấy giá trị lớn nhất trước, ta đảo dấu xác suất thành số âm: (-prob, u)
    pq = [(-1.0, s)]
    
    while pq:
        neg_p, u = heapq.heappop(pq)
        curr_p = -neg_p
        
        if curr_p < dist[u]: continue
        if u == t: return curr_p
        
        for v, prob_edge in adj[u]:
            # Thực hiện phép toán nhân xác suất và tìm giá trị lớn nhất (max)
            if dist[u] * prob_edge > dist[v]:
                dist[v] = dist[u] * prob_edge
                heapq.heappush(pq, (-dist[v], v))
                
    return dist[t]

if __name__ == "__main__":
    # Đồ thị lưới xác suất mẫu thử nghiệm
    prob_graph = [
        [(1, 0.8), (2, 0.5)],
        [(3, 0.9)],
        [(3, 0.95)],
        []
    ]
    print("Xác suất thành công lớn nhất từ 0 đến 3 là:", max_probability_path(prob_graph, 0, 3))