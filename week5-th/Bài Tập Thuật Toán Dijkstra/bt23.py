from __main__ import dijkstra_heap

class MultiQueryHandler:
    def __init__(self, adj):
        self.adj = adj
        self.n = len(adj)
        self.memo = {} # Sử dụng kỹ thuật Memoization để lưu kết quả các nguồn đã tính toán

    def query(self, s, t):
        # Nếu chưa từng tính toán Dijkstra cho nguồn s này, tiến hành chạy và lưu trữ
        if s not in self.memo:
            self.memo[s] = dijkstra_heap(self.adj, s)
        return self.memo[s][t]

if __name__ == "__main__":
    graph = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
    handler = MultiQueryHandler(graph)
    # Thực hiện các truy vấn lặp đi lặp lại một cách tối ưu nhất
    print("Truy vấn (0->4):", handler.query(0, 4))
    print("Truy vấn (0->5):", handler.query(0, 5))