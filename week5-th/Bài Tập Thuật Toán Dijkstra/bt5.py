import heapq

def dijkstra_undirected_g2():
    # Khởi tạo đồ thị vô hướng G2 (A=0, B=1, C=2, D=3, E=4)
    n = 5
    adj = [[] for _ in range(n)]
    
    edges = [
        (0, 1, 5), (0, 2, 3),  # A-B, A-C
        (1, 2, 1), (1, 3, 2),  # B-C, B-D
        (2, 3, 6),             # C-D
        (3, 4, 4)              # D-E
    ]
    
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    # Chạy Dijkstra từ nguồn s = 0 (đỉnh A)
    dist = [float('inf')] * n
    dist[0] = 0
    pq = [(0, 0)] # (khoảng cách, đỉnh u)
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    # Bản đồ tên đỉnh phục vụ cho việc in ấn định dạng chữ cái
    names = ['A', 'B', 'C', 'D', 'E']
    for i in range(n):
        print(f"Từ A tới {names[i]}: {dist[i]}")

if __name__ == "__main__":
    dijkstra_undirected_g2()