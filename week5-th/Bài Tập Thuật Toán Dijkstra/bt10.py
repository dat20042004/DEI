import time
import random

def benchmark():
    # Tạo đồ thị dày mô phỏng: V=1000, E xấp xỉ V^2
    V = 500
    adj_dense = [[] for _ in range(V)]
    for u in range(V):
        for v in range(V):
            if u != v:
                adj_dense[u].append((v, random.randint(1, 20)))
                
    # Đo thời gian bản O(V^2)
    from __main__ import dijkstra_v2, dijkstra_heap
    start = time.time()
    dijkstra_v2(adj_dense, 0)
    t1 = time.time() - start
    
    # Đo thời gian bản Heap O(E log V)
    start = time.time()
    dijkstra_heap(adj_dense, 0)
    t2 = time.time() - start
    
    print(f"Đồ thị dày (Dense Graph):")
    print(f"- Thời gian chạy bản O(V^2): {t1:.4f}s")
    print(f"- Thời gian chạy bản Heap: {t2:.4f}s")

if __name__ == "__main__":
    # Lưu ý: Hàm này cần liên kết với hàm ở Bài 3 và Bài 9 để hoạt động
    try:
        benchmark()
    except ImportError:
        print("Vui lòng gộp chung mã của bài 3 và bài 9 để chạy bài so sánh benchmark này.")