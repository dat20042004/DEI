
"""
CÂU 3 - Đồ thị & Thuật toán Dijkstra (cạnh trọng số âm)

Đề bài: Vì sao Dijkstra sai khi có cạnh âm? Tự thiết kế đồ thị 3 đỉnh làm
phản ví dụ, và đề xuất thuật toán thay thế.
"""

# GIẢI THÍCH:
# Dijkstra hoạt động theo nguyên tắc THAM LAM: mỗi bước chọn đỉnh u có
# khoảng cách tạm thời nhỏ nhất trong số các đỉnh CHƯA chốt, rồi "chốt"
# (finalize) khoảng cách đó và KHÔNG bao giờ xét lại đỉnh u nữa.
# Điều này chỉ đúng khi mọi trọng số cạnh đều KHÔNG ÂM, vì khi đó không có
# con đường nào đi qua đỉnh khác rồi quay lại có thể làm dist[u] nhỏ hơn nữa.
# Nếu có cạnh âm, một đỉnh có thể được chốt với khoảng cách CHƯA phải nhỏ
# nhất, và sau đó một cạnh âm dẫn tới nó lại bị bỏ qua vì nó đã "chốt".
#
# PHẢN VÍ DỤ (3 đỉnh): S=0, A=1, B=2
#   S -> B : 1     (cạnh trực tiếp, ngắn)
#   S -> A : 4
#   A -> B : -10   (cạnh âm)
# Đường đi thật sự ngắn nhất từ S tới B là  S->A->B = 4 + (-10) = -6
# nhưng Dijkstra sẽ chốt B = 1 ngay từ đầu (vì 1 < 4) và không xét lại.
#
# THUẬT TOÁN THAY THẾ: Bellman-Ford - chấp nhận cạnh âm, độ phức tạp O(V*E),
# và còn có thể phát hiện chu trình âm.

def dijkstra_chuan_khong_ho_tro_am(n, ke, s):
    """Dijkstra kiểu 'chốt đỉnh' cổ điển - dùng mảng visited, không xét lại đỉnh đã chốt."""
    dist = [float('inf')] * n
    dist[s] = 0
    da_chot = [False] * n
    for _ in range(n):
        u = -1
        for i in range(n):
            if not da_chot[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == float('inf'):
            break
        da_chot[u] = True                # <-- chốt đỉnh u, không xét lại nữa
        for v, w in ke[u]:
            if da_chot[v]:                # đỉnh v đã chốt -> KHÔNG cập nhật nữa (chỗ gây sai)
                continue
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


def bellman_ford(n, canh, s):
    """Thay thế Dijkstra khi có cạnh âm. canh: list các tuple (u, v, w)."""
    dist = [float('inf')] * n
    dist[s] = 0
    for _ in range(n - 1):
        for u, v, w in canh:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    co_chu_trinh_am = False
    for u, v, w in canh:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            co_chu_trinh_am = True
    return dist, co_chu_trinh_am


if __name__ == "__main__":
    # Đồ thị: 0=S, 1=A, 2=B
    ke = [[(1, 4), (2, 1)], [(2, -10)], []]
    canh = [(0, 1, 4), (0, 2, 1), (1, 2, -10)]

    ket_qua_dijkstra = dijkstra_chuan_khong_ho_tro_am(3, ke, 0)
    ket_qua_bellman, co_am = bellman_ford(3, canh, 0)

    print("Dijkstra (SAI khi có cạnh âm) =>", ket_qua_dijkstra)
    print("  -> dist[B] =", ket_qua_dijkstra[2], "(SAI, vì bỏ qua đường S->A->B)")
    print("Bellman-Ford (ĐÚNG)          =>", ket_qua_bellman)
    print("  -> dist[B] =", ket_qua_bellman[2], "(ĐÚNG, đi qua cạnh âm A->B)")