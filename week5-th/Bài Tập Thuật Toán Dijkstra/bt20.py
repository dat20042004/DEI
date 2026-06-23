import heapq

def k_shortest_paths(adj, s, t, k):
    n = len(adj)
    # Mảng đếm số lần mỗi đỉnh u được trích xuất ra khỏi hàng đợi ưu tiên
    count = [0] * n
    results = []
    
    pq = [(0, s)] # (quãng đường tích lũy, đỉnh hiện tại)
    
    while pq and count[t] < k:
        d, u = heapq.heappop(pq)
        count[u] += 1
        
        # Nếu đỉnh u là đích và số lần lấy ra chưa vượt quá K thì ghi nhận kết quả
        if u == t:
            results.append(d)
            
        if count[u] <= k:
            for v, w in adj[u]:
                heapq.heappush(pq, (d + w, v))
                
    return results

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    print("Top 3 độ dài đường đi ngắn nhất từ 0 tới 4:", k_shortest_paths(graph, 0, 4, 3))