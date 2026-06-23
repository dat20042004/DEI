# Khởi tạo danh sách kề cho đồ thị có hướng G1 gồm 6 đỉnh (0-5)
def build_graph_g1():
    n = 6
    adj = [[] for _ in range(n)]
    
    # Thêm các cạnh (đỉnh_đến, trọng_số) dựa trên hình ảnh G1
    adj[0] = [(1, 4), (2, 1)]
    adj[1] = [(3, 1)]
    adj[2] = [(1, 2), (3, 5), (4, 8)]
    adj[3] = [(4, 3), (5, 6)]
    adj[4] = [(5, 2)]
    adj[5] = []
    
    return adj

# Chạy thử nghiệm in danh sách kề
if __name__ == "__main__":
    graph = build_graph_g1()
    for i, neighbors in enumerate(graph):
        print(f"adj[{i}] = {neighbors}")