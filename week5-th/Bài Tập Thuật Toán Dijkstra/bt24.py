import heapq

def a_star_grid(grid, src, dst):
    rows, cols = len(grid), len(grid[0])
    
    # Hàm Heuristic tính toán khoảng cách Manhattan (Admissible Heuristic)
    def heuristic(r, c):
        return abs(r - dst[0]) + abs(c - dst[1])
        
    # Chứa trạng thái lưu trữ: f_score = g_score + h_score
    g_score = [[float('inf')] * cols for _ in range(rows)]
    g_score[src[0]][src[1]] = grid[src[0]][src[1]]
    
    # Lưu định dạng cặp tuple trong PQ: (f_score, r, c)
    pq = [(grid[src[0]][src[1]] + heuristic(src[0], src[1]), src[0], src[1])]
    visited_nodes_count = 0
    
    while pq:
        f, r, c = heapq.heappop(pq)
        visited_nodes_count += 1
        
        if (r, c) == dst:
            return g_score[r][c], visited_nodes_count
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                tentative_g = g_score[r][c] + grid[nr][nc]
                if tentative_g < g_score[nr][nc]:
                    g_score[nr][nc] = tentative_g
                    f_next = tentative_g + heuristic(nr, nc)
                    heapq.heappush(pq, (f_next, nr, nc))
                    
    return -1, visited_nodes_count

if __name__ == "__main__":
    matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    cost, steps = a_star_grid(matrix, (0, 0), (2, 2))
    print(f"Thuật toán A* giải quyết lưới chi phí: {cost} (Số đỉnh đã duyệt qua: {steps})")