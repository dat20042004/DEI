def dijkstra_step_by_step():
    # Đồ thị G1 từ bài 1
    adj = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    n = 6
    
    dist = [float('inf')] * n
    dist[0] = 0
    visited = [False] * n
    order_of_execution = []
    
    print(f"{'Vòng':<6}{'Chốt':<6}{'Mảng dist[] hiện tại'}")
    print("-" * 35)
    print(f"{'0':<6}{'-':<6}{dist}")
    
    for step in range(n):
        # Chọn đỉnh chưa chốt có khoảng cách nhỏ nhất
        u = -1
        min_d = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
                
        if u == -1: break
        
        visited[u] = True
        order_of_execution.append(u)
        
        # Nới lỏng các cạnh kề u
        for v, w in adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
        print(f"{step + 1:<6}{u:<6}{dist}")
        
    print("-" * 35)
    print("Thứ tự các đỉnh được chốt:", order_of_execution)

if __name__ == "__main__":
    dijkstra_step_by_step()