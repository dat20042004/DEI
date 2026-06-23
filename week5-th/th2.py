import sys


class Graph:

    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        print("Đỉnh nguồn xuất phát từ đỉnh:", a)
        for nut in range(cung.x):
            print(a, "đến đỉnh", nut, "độ dài đường đi là:", L[nut])

    def duongdinhonhat(cung, L, P):
        min_val = sys.maxsize
        min_index = -1
        for x in range(cung.x):
            if L[x] < min_val and P[x] == False:
                min_val = L[x]
                min_index = x
        return min_index

    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x
        L[a] = 0
        P = [False] * cung.x

        for cout in range(cung.x):
            u = cung.duongdinhonhat(L, P)

            # Trường hợp đồ thị bị ngắt kết nối, không tìm thấy đỉnh tiếp theo
            if u == -1:
                break

            P[u] = True

            for x in range(cung.x):
                if (
                    cung.graph[u][x] > 0
                    and P[x] == False
                    and L[x] > L[u] + cung.graph[u][x]
                ):
                    L[x] = L[u] + cung.graph[u][x]

        cung.inketqua(L, a)


# Khởi tạo đồ thị có 6 đỉnh
g = Graph(6)

# Khai báo ma trận kề theo dữ liệu của bạn
g.graph = [
    [0, 5, 0, 10, 0, 0],
    [5, 0, 15, 2, 0, 0],
    [0, 15, 0, 0, 1, 12],
    [10, 2, 0, 0, 6, 0],
    [0, 0, 1, 6, 0, 7],
    [0, 0, 12, 0, 7, 0],
]

# Chạy thuật toán tìm đường đi ngắn nhất bắt đầu từ đỉnh 0
g.timduongdi(0)