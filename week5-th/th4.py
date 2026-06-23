import sys


class Graph:

    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        ten_dinh = ["a", "b", "c", "f", "g", "z"]
        print(f"--- Đỉnh nguồn xuất phát từ: {ten_dinh[a]} ---")
        for nut in range(cung.x):
            khoang_cach = (
                L[nut] if L[nut] != sys.maxsize else "Không thể đến"
            )
            print(
                f"Từ {ten_dinh[a]} đến đỉnh {ten_dinh[nut]} -> Độ dài đường đi ngắn nhất là: {khoang_cach}"
            )

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


# Khởi tạo đồ thị 6 đỉnh (a, b, c, f, g, z)
g = Graph(6)

# Câu a) Ma trận kề từ đồ thị có hướng trong hình
# Thứ tự dòng/cột: [a, b, c, f, g, z]
g.graph = [
    [0, 3, 0, 1, 0, 0],  # a -> b(3), a -> f(1)
    [0, 0, 7, 0, 0, 0],  # b -> c(7)
    [0, 0, 0, 0, 0, 3],  # c -> z(3)
    [0, 0, 9, 0, 2, 0],  # f -> c(9), f -> g(2)
    [0, 0, 3, 0, 0, 7],  # g -> c(3), g -> z(7)
    [0, 0, 0, 0, 0, 0],  # z không đi sang đỉnh nào
]

# Câu b) Tìm đường đi ngắn nhất từ đỉnh a (đỉnh số 0)
g.timduongdi(0)