# Gọi thuật toán Dijkstra thông thường từ bài 9
from __main__ import dijkstra_heap

def path_via_mandatory_node(adj, s, t, k):
    # Tính từ s sang mọi đỉnh và từ k sang mọi đỉnh
    dist_from_s = dijkstra_heap(adj, s)
    dist_from_k = dijkstra_heap(adj, k)
    
    # Tổng quãng đường bắt buộc đi qua k
    total_cost = dist_from_s[k] + dist_from_k[t]
    return total_cost

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    # Tìm đường ngắn nhất từ 0 tới 5 bắt buộc qua 2
    print("Tổng độ dài đi từ 0 -> 2 -> 5 là:", path_via_mandatory_node(graph, 0, 5, 2))