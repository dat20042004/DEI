import heapq

def dijkstra_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Ma trận khoảng cách
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]
    
    pq = [(grid[0][0], 0, 0)] # (chi phí, r, c)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Di chuyển 4 hướng
    
    while pq:
        d, r, c = heapq.heappop(pq)
        if d > dist[r][c]: continue
        if r == rows - 1 and c == cols - 1: return d
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if d + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = d + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))
    return -1

if __name__ == "__main__":
    matrix = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print("Tổng chi phí nhỏ nhất đi qua lưới là:", dijkstra_grid(matrix))