import heapq

def dijkstra_extended_state(adj, s, t, max_fuel, fuel_costs):
    # Trạng thái mở rộng gồm 2 yếu tố: (đỉnh_u, lượng_nhiên_liệu_còn_lại)
    # Khởi tạo bảng khoảng cách lưu trữ: dist[u][nhiên_liệu]
    n = len(adj)
    dist = [[float('inf')] * (max_fuel + 1) for _ in range(n)]
    
    dist[s][max_fuel] = 0
    pq = [(0, s, max_fuel)] # (chi phí, đỉnh, nhiên liệu)
    
    while pq:
        cost, u, fuel = heapq.heappop(pq)
        if cost > dist[u][fuel]: continue
        if u == t: return cost
        
        # Option 1: Thử nạp thêm 1 đơn vị nhiên liệu tại trạm u hiện tại nếu chưa đầy bình
        if fuel < max_fuel:
            if cost + fuel_costs[u] < dist[u][fuel + 1]:
                dist[u][fuel + 1] = cost + fuel_costs[u]
                heapq.heappush(pq, (dist[u][fuel + 1], u, fuel + 1))
                
        # Option 2: Di chuyển sang các đỉnh kề v lân cận
        for v, w in adj[u]:
            if fuel >= w: # Chỉ có thể đi nếu lượng xăng còn lại đủ lớn hơn trọng số cạnh w
                if cost < dist[v][fuel - w]:
                    dist[v][fuel - w] = cost
                    heapq.heappush(pq, (cost, v, fuel - w))
                    
    return -1

if __name__ == "__main__":
    # Đồ thị kiểm thử giả lập bài toán nhiên liệu xe
    graph = [[(1, 2)], [(2, 3)], []]
    fuel_prices = [5, 2, 1]
    print("Chi phí di chuyển tối ưu trên đồ thị mở rộng:", dijkstra_extended_state(graph, 0, 2, 5, fuel_prices))