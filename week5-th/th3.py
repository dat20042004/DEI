import sys


class Graph:

    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        print("đỉnh nguồn xuất phát từ: ")
        for nut in range(cung.x):
            khoang_cach = (
                L[nut] if L[nut] != sys.maxsize else "Không thể đến"
            )
            print(a, " đến đỉnh ", nut, "độ dài đường đi là: ", khoang_cach)

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

            # Phòng trường hợp đồ thị có đỉnh không liên thông
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


# Khởi tạo đồ thị 6 đỉnh
g = Graph(6)

# Khai báo ma trận kề mới theo yêu cầu của bạn
g.graph = [
    [0, 7, 0, 14, 0, 0],
    [0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 1, 0, 5, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0],
]

# Chạy thuật toán xuất phát từ đỉnh 0
g.timduongdi(0)