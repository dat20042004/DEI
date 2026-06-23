import heapq

def second_shortest_path(adj, s, t):
    n = len(adj)
    # Khởi tạo ma trận lưu 2 trạng thái khoảng cách: dist[u][0] (ngắn nhất), dist[u][1] (ngắn nhì)
    dist = [[float('inf'), float('inf')] for _ in range(n)]
    
    dist[s][0] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        for v, w in adj[u]:
            new_cost = d + w
            # Trường hợp 1: Tốt hơn cả khoảng cách tốt nhất hiện tại
            if new_cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = new_cost
                heapq.heappush(pq, (new_cost, v))
            # Trường hợp 2: Lớn hơn khoảng cách thứ nhất nhưng tốt hơn khoảng cách thứ hai
            elif dist[v][0] < new_cost < dist[v][1]:
                dist[v][1] = new_cost
                heapq.heappush(pq, (new_cost, v))
                
    return dist[t][1]

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    print("Độ dài đường đi ngắn nhì từ 0 đến 4 là:", second_shortest_path(graph, 0, 4))