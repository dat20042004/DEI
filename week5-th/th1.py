import sys


class Graph:

    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(cung, L, a):
        # Danh sách nhãn đỉnh để in ra màn hình cho dễ đọc
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
            # Tìm đỉnh có khoảng cách nhỏ nhất và chưa được duyệt (P[x] == False)
            if L[x] < min_val and P[x] == False:
                min_val = L[x]
                min_index = x

        return min_index  # Đã sửa thụt lề: Đưa ra ngoài vòng lặp for

    def timduongdi(cung, a):
        # L lưu khoảng cách ngắn nhất từ đỉnh nguồn 'a' đến các đỉnh còn lại
        L = [sys.maxsize] * cung.x
        L[a] = 0  # Khoảng cách từ 'a' đến chính nó bằng 0

        # P lưu trạng thái đỉnh đã được duyệt hay chưa (True: đã duyệt, False: chưa)
        P = [False] * cung.x

        for cout in range(cung.x):
            # Chọn đỉnh u chưa duyệt có khoảng cách ngắn nhất
            u = cung.duongdinhonhat(L, P)

            # Nếu không tìm thêm được đỉnh nào hợp lệ, dừng vòng lặp
            if u == -1:
                break

            # Đánh dấu đỉnh u đã được duyệt
            P[u] = True

            # Cập nhật giá trị khoảng cách cho các đỉnh hàng xóm của u
            for x in range(cung.x):
                if (
                    cung.graph[u][x] > 0
                    and P[x] == False
                    and L[x] > L[u] + cung.graph[u][x]
                ):
                    L[x] = L[u] + cung.graph[u][x]

        cung.inketqua(L, a)


# Khởi tạo đồ thị có 6 đỉnh (a, b, c, f, g, z)
g = Graph(6)

# Ma trận kề chuẩn hóa theo đúng hình vẽ:
# Các cột/dòng tương ứng theo thứ tự: [a, b, c, f, g, z]
g.graph = [
    [0, 3, 0, 1, 0, 0],  # a nối với b(3), f(1)
    [3, 0, 5, 2, 0, 0],  # b nối với a(3), c(5), f(2)
    [0, 5, 0, 0, 4, 2],  # c nối với b(5), g(4), z(2)
    [1, 2, 0, 0, 6, 0],  # f nối với a(1), b(2), g(6)
    [0, 0, 4, 6, 0, 7],  # g nối với c(4), f(6), z(7)
    [0, 0, 2, 0, 7, 0],  # z nối với c(2), g(7)
]

# Chạy thuật toán xuất phát từ đỉnh số 0 (đỉnh 'a')
g.timduongdi(0)  # Đã sửa lỗi chính tả từ 'tomduongdi' thành 'timduongdi'