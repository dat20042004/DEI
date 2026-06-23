import sys


class Graph:

    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        ten_dinh = ["a", "b", "c", "d", "e", "z"]
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


# Khởi tạo đồ thị 6 đỉnh (a, b, c, d, e, z) theo Hình 2
g = Graph(6)

# Ma trận kề từ đồ thị có hướng (Hình 2)
# Thứ tự dòng/cột: [a, b, c, d, e, z]
g.graph = [
    [0, 2, 0, 5, 0, 0],  # a -> b(2), a -> d(5)
    [0, 0, 7, 0, 1, 0],  # b -> c(7), b -> e(1)
    [0, 0, 0, 0, 0, 1],  # c -> z(1)
    [0, 0, 0, 0, 6, 0],  # d -> e(6) (trọng số 6 mờ nằm giữa d và e)
    [0, 0, 3, 0, 0, 2],  # e -> c(3), e -> z(2)
    [0, 0, 0, 0, 0, 0],  # z không đi sang đỉnh nào
]

# Tìm đường đi ngắn nhất từ đỉnh a (đỉnh số 0)
g.timduongdi(0)