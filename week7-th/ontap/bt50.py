# -*- coding: utf-8 -*-
"""
Đề Ôn Tập Tổng Hợp - 50 Câu
Cấu trúc dữ liệu & Giải thuật
Code đơn giản, dễ hiểu, có comment tiếng Việt.
"""

import heapq
import random
from collections import deque, OrderedDict


# =====================================================================
# PHẦN 1 - TÌM KIẾM NHỊ PHÂN (Câu 1 - 6)
# =====================================================================

# Câu 1: Tìm kiếm nhị phân cơ bản
def tim_kiem_nhi_phan(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# Câu 2: Vị trí đầu / cuối & đếm số lần xuất hiện
def tim_vi_tri_dau(a, x):
    lo, hi = 0, len(a) - 1
    ket_qua = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            ket_qua = mid
            hi = mid - 1          # tìm tiếp bên trái
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return ket_qua


def tim_vi_tri_cuoi(a, x):
    lo, hi = 0, len(a) - 1
    ket_qua = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            ket_qua = mid
            lo = mid + 1          # tìm tiếp bên phải
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return ket_qua


def dem_so_lan_xuat_hien(a, x):
    dau = tim_vi_tri_dau(a, x)
    if dau == -1:
        return 0
    cuoi = tim_vi_tri_cuoi(a, x)
    return cuoi - dau + 1


# Câu 3: Lower bound & Upper bound
def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# Câu 4: Tìm kiếm trong mảng xoay
def tim_kiem_mang_xoay(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        if a[lo] <= a[mid]:                      # nửa trái đang sắp xếp
            if a[lo] <= x < a[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                     # nửa phải đang sắp xếp
            if a[mid] < x <= a[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# Câu 5: Koko ăn chuối (Binary search trên đáp án)
def koko_an_chuoi(piles, h):
    def so_gio_can(toc_do):
        return sum((p + toc_do - 1) // toc_do for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if so_gio_can(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


# Câu 6: Chia mảng thành k đoạn sao cho tổng lớn nhất là nhỏ nhất
def chia_mang_nho_nhat(a, k):
    def dem_so_doan(gioi_han):
        so_doan = 1
        tong = 0
        for x in a:
            if tong + x > gioi_han:
                so_doan += 1
                tong = x
            else:
                tong += x
        return so_doan

    lo, hi = max(a), sum(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if dem_so_doan(mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


# =====================================================================
# PHẦN 2 - THUẬT TOÁN SẮP XẾP (Câu 7 - 14)
# =====================================================================

# Câu 7: Bubble sort & đếm số swap
def bubble_sort(a):
    a = a[:]
    n = len(a)
    dem_swap = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                dem_swap += 1
    return a, dem_swap
    # Số swap luôn bằng đúng số cặp nghịch thế (i<j nhưng a[i]>a[j])
    # vì mỗi swap chỉ đổi chỗ đúng 1 cặp liền kề đang bị nghịch thế.


# Câu 8: Bubble sort tối ưu (dừng sớm khi không còn swap)
def bubble_sort_toi_uu(a):
    a = a[:]
    n = len(a)
    so_luot = 0
    for i in range(n):
        so_luot += 1
        da_doi_cho = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_doi_cho = True
        if not da_doi_cho:
            break
    return a, so_luot


# Câu 9: Insertion sort & đếm số lần shift
def insertion_sort(a):
    a = a[:]
    n = len(a)
    so_shift = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            so_shift += 1
        a[j + 1] = key
    return a, so_shift
    # Số shift cũng đúng bằng số cặp nghịch thế, giống bubble sort.


# Câu 10: Binary insertion sort (dùng tìm nhị phân để tìm vị trí chèn)
def binary_insertion_sort(a):
    a = a[:]
    n = len(a)
    so_shift = 0
    for i in range(1, n):
        key = a[i]
        lo, hi = 0, i
        while lo < hi:                 # tìm vị trí chèn bằng nhị phân O(log i)
            mid = (lo + hi) // 2
            if a[mid] <= key:
                lo = mid + 1
            else:
                hi = mid
        j = i - 1
        while j >= lo:
            a[j + 1] = a[j]
            j -= 1
            so_shift += 1
        a[lo] = key
    return a, so_shift
    # So sánh giảm còn O(log i) nhưng số shift KHÔNG đổi (vẫn phải dời phần tử).


# Câu 11: Selection sort & đếm số so sánh
def selection_sort(a):
    a = a[:]
    n = len(a)
    so_sanh = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            so_sanh += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, so_sanh
    # Luôn duyệt hết phần còn lại để tìm min -> luôn có n(n-1)/2 phép so sánh,
    # kể cả khi mảng đã sắp xếp sẵn (không có best case nhanh hơn).


# Câu 12: So sánh tính ổn định của 3 thuật toán
# - Bubble sort: ỔN ĐỊNH (chỉ đổi chỗ khi a[j] > a[j+1], phần tử bằng nhau giữ nguyên thứ tự)
# - Insertion sort: ỔN ĐỊNH (chỉ dời khi a[j] > key, phần tử bằng nhau không bị vượt qua)
# - Selection sort: KHÔNG ỔN ĐỊNH (đổi chỗ trực tiếp min_idx và i có thể đổi thứ tự 2 phần tử bằng nhau)
def vi_du_selection_khong_on_dinh():
    # mỗi phần tử là (giá_trị, nhãn) để thấy rõ thứ tự bị đảo
    a = [(3, 'A'), (3, 'B'), (1, 'C')]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a  # -> [(1,'C'), (3,'B'), (3,'A')]  hai phần tử giá trị 3 bị đổi thứ tự


# Câu 13: Đếm nghịch thế O(n log n) bằng merge sort
def dem_nghich_the(a):
    def merge_va_dem(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        trai, dem1 = merge_va_dem(arr[:mid])
        phai, dem2 = merge_va_dem(arr[mid:])
        ket_qua = []
        i = j = 0
        dem = dem1 + dem2
        while i < len(trai) and j < len(phai):
            if trai[i] <= phai[j]:
                ket_qua.append(trai[i])
                i += 1
            else:
                ket_qua.append(phai[j])
                j += 1
                dem += len(trai) - i     # tất cả phần tử còn lại của "trai" đều > phai[j]
        ket_qua.extend(trai[i:])
        ket_qua.extend(phai[j:])
        return ket_qua, dem

    _, tong = merge_va_dem(a)
    return tong


# Câu 14: Shell sort
def shell_sort(a):
    a = a[:]
    n = len(a)
    gap = n // 2
    so_shift = 0
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
                so_shift += 1
            a[j] = temp
        gap //= 2
    return a, so_shift


# =====================================================================
# PHẦN 3 - ĐỒ THỊ & DIJKSTRA (Câu 15 - 20)
# =====================================================================

# Câu 15: Dijkstra cơ bản (dùng heap luôn, ke là danh sách kề)
def dijkstra(n, ke, s):
    dist = [float('inf')] * n
    dist[s] = 0
    hang_doi = [(0, s)]
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        if d > dist[u]:
            continue
        for v, w in ke[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(hang_doi, (dist[v], v))
    return dist


# Câu 16: Dijkstra có truy vết đường đi bằng parent[]
def dijkstra_truy_vet(n, ke, s):
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[s] = 0
    hang_doi = [(0, s)]
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        if d > dist[u]:
            continue
        for v, w in ke[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(hang_doi, (dist[v], v))
    return dist, parent


def in_duong_di(parent, s, t):
    duong_di = []
    cur = t
    while cur != -1:
        duong_di.append(cur)
        if cur == s:
            break
        cur = parent[cur]
    duong_di.reverse()
    return duong_di


# Câu 17: Dijkstra dùng min-heap - chính là hàm dijkstra() ở Câu 15
# Độ phức tạp O((V+E) log V), phù hợp đồ thị thưa vì chỉ xử lý các cạnh thực sự tồn tại
# thay vì duyệt toàn bộ ma trận kề O(V^2).


# Câu 18: Vì sao Dijkstra cần trọng số không âm + thay thế bằng Bellman-Ford
def bellman_ford(n, canh, s):
    # canh: list các tuple (u, v, w)
    dist = [float('inf')] * n
    dist[s] = 0
    for _ in range(n - 1):
        for u, v, w in canh:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # kiểm tra chu trình âm
    co_chu_trinh_am = False
    for u, v, w in canh:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            co_chu_trinh_am = True
    return dist, co_chu_trinh_am
    # Giải thích: Dijkstra "chốt" đỉnh u ngay khi lấy ra khỏi hàng đợi với giả định
    # không còn đường nào ngắn hơn dist[u] nữa. Nếu có cạnh âm, một đường đi qua
    # đỉnh khác (được xử lý sau) có thể tạo ra khoảng cách ngắn hơn, phá vỡ giả định đó.
    # => Dùng Bellman-Ford (chấp nhận cạnh âm, phát hiện chu trình âm), O(V*E).


# Câu 19: Đường đi ngắn nhất trên lưới (Dijkstra trên đồ thị lưới)
def duong_di_luoi(luoi):
    rows = len(luoi)
    cols = len(luoi[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = luoi[0][0]
    hang_doi = [(luoi[0][0], 0, 0)]
    huong = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while hang_doi:
        d, x, y = heapq.heappop(hang_doi)
        if d > dist[x][y]:
            continue
        for dx, dy in huong:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                nd = d + luoi[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(hang_doi, (nd, nx, ny))
    return dist[rows - 1][cols - 1]


# Câu 20: So sánh Dijkstra vs Bellman-Ford vs A*
# | Thuật toán     | Cạnh âm?  | Độ phức tạp        | Ghi chú                          |
# |----------------|-----------|--------------------|-----------------------------------|
# | Dijkstra       | Không     | O((V+E) log V)     | Nhanh, cần trọng số không âm       |
# | Bellman-Ford   | Có        | O(V * E)           | Chậm hơn, phát hiện chu trình âm   |
# | A*             | Không     | phụ thuộc heuristic| Dùng thêm hàm ước lượng h(v) tới   |
# |                |           |                    | đích, nếu heuristic tốt (admissible)|
# |                |           |                    | thì duyệt ít đỉnh hơn Dijkstra.    |


# =====================================================================
# PHẦN 4 - NGĂN XẾP (STACK) (Câu 21 - 25)
# =====================================================================

# Câu 21: Kiểm tra dấu ngoặc cân bằng
def dau_ngoac_can_bang(s):
    ngan_xep = []
    doi = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            ngan_xep.append(c)
        elif c in ')]}':
            if not ngan_xep or ngan_xep.pop() != doi[c]:
                return False
    return len(ngan_xep) == 0


# Câu 22: Min Stack - getMin() trong O(1)
class MinStack:
    def __init__(self):
        self.ngan_xep = []
        self.ngan_xep_min = []

    def push(self, x):
        self.ngan_xep.append(x)
        if not self.ngan_xep_min or x <= self.ngan_xep_min[-1]:
            self.ngan_xep_min.append(x)
        else:
            self.ngan_xep_min.append(self.ngan_xep_min[-1])

    def pop(self):
        self.ngan_xep_min.pop()
        return self.ngan_xep.pop()

    def get_min(self):
        return self.ngan_xep_min[-1]


# Câu 23: Tính biểu thức hậu tố (RPN)
def tinh_hau_to(bieu_thuc):
    ngan_xep = []
    for token in bieu_thuc.split():
        if token in ('+', '-', '*', '/'):
            b = ngan_xep.pop()
            a = ngan_xep.pop()
            if token == '+':
                ngan_xep.append(a + b)
            elif token == '-':
                ngan_xep.append(a - b)
            elif token == '*':
                ngan_xep.append(a * b)
            else:
                ngan_xep.append(int(a / b))
        else:
            ngan_xep.append(int(token))
    return ngan_xep[-1]


# Câu 24: Next Greater Element (dùng stack đơn điệu)
def next_greater_element(a):
    n = len(a)
    ket_qua = [-1] * n
    ngan_xep = []              # lưu chỉ số, giá trị giảm dần từ đáy lên đỉnh
    for i in range(n):
        while ngan_xep and a[ngan_xep[-1]] < a[i]:
            idx = ngan_xep.pop()
            ket_qua[idx] = a[i]
        ngan_xep.append(i)
    return ket_qua


# Câu 25: Diện tích hình chữ nhật lớn nhất trong histogram
def histogram_lon_nhat(h):
    ngan_xep = []
    max_area = 0
    h2 = h + [0]               # thêm cột chiều cao 0 để "xả" hết stack ở cuối
    for i, height in enumerate(h2):
        while ngan_xep and h2[ngan_xep[-1]] > height:
            top = ngan_xep.pop()
            chieu_cao = h2[top]
            chieu_rong = i if not ngan_xep else i - ngan_xep[-1] - 1
            max_area = max(max_area, chieu_cao * chieu_rong)
        ngan_xep.append(i)
    return max_area


# =====================================================================
# PHẦN 5 - HÀNG ĐỢI (QUEUE) (Câu 26 - 30)
# =====================================================================

# Câu 26: Hàng đợi FIFO cơ bản & hàng đợi vòng (circular)
class HangDoiVong:
    def __init__(self, size):
        self.a = [None] * size
        self.size = size
        self.dau = 0
        self.cuoi = 0
        self.count = 0

    def enqueue(self, x):
        if self.count == self.size:
            print("Hàng đợi đầy")
            return
        self.a[self.cuoi] = x
        self.cuoi = (self.cuoi + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Hàng đợi rỗng")
            return None
        x = self.a[self.dau]
        self.dau = (self.dau + 1) % self.size
        self.count -= 1
        return x


# Câu 27: Queue mô phỏng bằng 2 stack
class QueueBangHaiStack:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x):
        self.stack_in.append(x)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop() if self.stack_out else None
    # Amortized O(1): mỗi phần tử chỉ bị di chuyển từ stack_in sang stack_out
    # đúng 1 lần trong suốt vòng đời của nó, nên tổng chi phí cho n thao tác là O(n).


# Câu 28: BFS dùng hàng đợi
def bfs(n, ke, start):
    da_tham = [False] * n
    hang_doi = deque([start])
    da_tham[start] = True
    thu_tu_tham = []
    while hang_doi:
        u = hang_doi.popleft()
        thu_tu_tham.append(u)
        for v in ke[u]:
            if not da_tham[v]:
                da_tham[v] = True
                hang_doi.append(v)
    return thu_tu_tham


# Câu 29: Giá trị lớn nhất trong cửa sổ trượt (deque đơn điệu)
def max_cua_so_truot(a, k):
    dq = deque()                # lưu chỉ số, giá trị giảm dần từ đầu tới cuối deque
    ket_qua = []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:      # phần tử ngoài cửa sổ
            dq.popleft()
        if i >= k - 1:
            ket_qua.append(a[dq[0]])
    return ket_qua


# Câu 30: Lập lịch Round-Robin
def round_robin(processes, quantum):
    # processes: list các tuple (ten, burst_time)
    hang_doi = deque([(ten, bt) for ten, bt in processes])
    thoi_gian = 0
    hoan_thanh = {}
    while hang_doi:
        ten, bt = hang_doi.popleft()
        chay = min(bt, quantum)
        thoi_gian += chay
        bt -= chay
        if bt == 0:
            hoan_thanh[ten] = thoi_gian
        else:
            hang_doi.append((ten, bt))
    return hoan_thanh


# =====================================================================
# PHẦN 6 - ARRAY LIST (Câu 31 - 35)
# =====================================================================

# Câu 31: Mảng động - resize gấp đôi khi đầy
class MangDong:
    def __init__(self):
        self.a = [None] * 1
        self.size = 0
        self.capacity = 1

    def append(self, x):
        if self.size == self.capacity:
            self.capacity *= 2
            moi = [None] * self.capacity
            for i in range(self.size):
                moi[i] = self.a[i]
            self.a = moi
        self.a[self.size] = x
        self.size += 1
    # Amortized O(1): resize chỉ xảy ra tại các lần append thứ 1,2,4,8,...
    # tổng chi phí copy cho n lần append là 1+2+4+...+n ~ 2n = O(n) -> trung bình O(1)/lần.


# Câu 32: removeIf tại chỗ, giữ thứ tự, O(n), 2 con trỏ
def remove_if(a, dieu_kien):
    write = 0
    for read in range(len(a)):
        if not dieu_kien(a[read]):
            a[write] = a[read]
            write += 1
    del a[write:]
    return a


# Câu 33: Xoay mảng sang phải k vị trí (kỹ thuật đảo 3 lần)
def xoay_mang(a, k):
    n = len(a)
    k = k % n
    def dao_nguoc(l, r):
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    dao_nguoc(0, n - 1)
    dao_nguoc(0, k - 1)
    dao_nguoc(k, n - 1)
    return a


# Câu 34: Loại bỏ trùng lặp, giữ thứ tự xuất hiện đầu tiên
def loai_trung_lap_On2(a):
    ket_qua = []
    for x in a:
        if x not in ket_qua:      # kiểm tra "in" trên list là O(n) -> tổng O(n^2)
            ket_qua.append(x)
    return ket_qua


def loai_trung_lap_On(a):
    da_thay = set()
    ket_qua = []
    for x in a:
        if x not in da_thay:      # kiểm tra "in" trên set là O(1) -> tổng O(n)
            da_thay.add(x)
            ket_qua.append(x)
    return ket_qua


# Câu 35: Merge Intervals - gộp các khoảng giao nhau
def merge_intervals(khoang):
    khoang = sorted(khoang, key=lambda x: x[0])
    ket_qua = [list(khoang[0])]
    for start, end in khoang[1:]:
        if start <= ket_qua[-1][1]:
            ket_qua[-1][1] = max(ket_qua[-1][1], end)
        else:
            ket_qua.append([start, end])
    return ket_qua


# =====================================================================
# PHẦN 7 - LINKED LIST (Câu 36 - 41)
# =====================================================================

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def tao_linked_list(values):
    dummy = Node(0)
    cur = dummy
    for v in values:
        cur.next = Node(v)
        cur = cur.next
    return dummy.next


def in_linked_list(head):
    ket_qua = []
    while head:
        ket_qua.append(head.val)
        head = head.next
    return ket_qua


# Câu 36: Đảo ngược singly linked list - lặp & đệ quy
def dao_nguoc_lap(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def dao_nguoc_de_quy(head):
    if head is None or head.next is None:
        return head
    new_head = dao_nguoc_de_quy(head.next)
    head.next.next = head
    head.next = None
    return new_head


# Câu 37: Tìm nút giữa (con trỏ nhanh/chậm)
def tim_nut_giua(head):
    cham = head
    nhanh = head
    while nhanh and nhanh.next:
        cham = cham.next
        nhanh = nhanh.next.next
    return cham


# Câu 38: Phát hiện chu trình & tìm nút bắt đầu chu trình (Floyd)
def tim_dau_chu_trinh(head):
    cham = head
    nhanh = head
    while nhanh and nhanh.next:
        cham = cham.next
        nhanh = nhanh.next.next
        if cham == nhanh:               # phát hiện chu trình
            p = head
            while p != cham:            # giai đoạn 2: tìm điểm bắt đầu
                p = p.next
                cham = cham.next
            return p
    return None


# Câu 39: Xóa nút thứ k từ cuối (2 con trỏ cách nhau k bước)
def xoa_nut_thu_k_tu_cuoi(head, k):
    dummy = Node(0)
    dummy.next = head
    nhanh = dummy
    cham = dummy
    for _ in range(k):
        nhanh = nhanh.next
    while nhanh.next:
        nhanh = nhanh.next
        cham = cham.next
    cham.next = cham.next.next
    return dummy.next


# Câu 40: Sắp xếp linked list bằng merge sort O(n log n)
def sap_xep_linked_list(head):
    if head is None or head.next is None:
        return head
    cham = head
    nhanh = head.next
    while nhanh and nhanh.next:
        cham = cham.next
        nhanh = nhanh.next.next
    phai = cham.next
    cham.next = None
    trai = sap_xep_linked_list(head)
    phai = sap_xep_linked_list(phai)
    return tron_hai_list(trai, phai)


def tron_hai_list(a, b):
    dummy = Node(0)
    cur = dummy
    while a and b:
        if a.val <= b.val:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next
        cur = cur.next
    cur.next = a if a else b
    return dummy.next


# Câu 41: LRU Cache - get/put O(1) bằng doubly linked list + hash table
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = OrderedDict()   # OrderedDict dùng doubly linked list + hash table bên trong

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)   # đẩy lên "mới nhất"
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.cap:
            self.data.popitem(last=False)   # xóa phần tử cũ nhất


# =====================================================================
# PHẦN 8 - BẢNG BĂM (HASH TABLE) (Câu 42 - 46)
# =====================================================================

# Câu 42: Chaining & Open addressing (linear probing)
class HashChaining:
    def __init__(self, size=10):
        self.size = size
        self.bang = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for cap in self.bang[idx]:
            if cap[0] == key:
                cap[1] = value
                return
        self.bang[idx].append([key, value])

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.bang[idx]:
            if k == key:
                return v
        return None

    def remove(self, key):
        idx = self._hash(key)
        self.bang[idx] = [cap for cap in self.bang[idx] if cap[0] != key]
    # Bộ nhớ: chaining tốn thêm bộ nhớ cho các node/list ở mỗi bucket.
    # Khi tải cao: chaining vẫn hoạt động tốt (chỉ chậm dần theo chiều dài list),
    # còn linear probing bị "cụm" (clustering) làm chậm đáng kể.
    # Xóa: chaining xóa trực tiếp; linear probing phải đánh dấu "đã xóa" (tombstone)
    # để không làm gãy chuỗi probing.


class HashLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        while self.keys[idx] is not None and self.keys[idx] != key:
            idx = (idx + 1) % self.size
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
            if idx == start:
                break
        return None


# Câu 43: Load factor & rehashing
class HashRehash:
    def __init__(self, size=4):
        self.size = size
        self.count = 0
        self.bang = [[] for _ in range(size)]

    def _hash(self, key, size):
        return hash(key) % size

    def put(self, key, value):
        idx = self._hash(key, self.size)
        for cap in self.bang[idx]:
            if cap[0] == key:
                cap[1] = value
                return
        self.bang[idx].append([key, value])
        self.count += 1
        if self.count / self.size > 0.75:      # load factor vượt ngưỡng
            self._rehash()

    def _rehash(self):
        old = self.bang
        self.size *= 2
        self.bang = [[] for _ in range(self.size)]
        for danh_sach in old:
            for k, v in danh_sach:
                idx = self._hash(k, self.size)
                self.bang[idx].append([k, v])


# Câu 44: Two Sum dùng hash
def two_sum(a, target):
    da_thay = {}
    for i, x in enumerate(a):
        bu = target - x
        if bu in da_thay:
            return (da_thay[bu], i)
        da_thay[x] = i
    return None


# Câu 45: Đếm số đoạn con liên tiếp có tổng bằng k (tổng tiền tố + hash)
def dem_doan_con_tong_bang_k(a, k):
    dem = {0: 1}
    tong = 0
    ket_qua = 0
    for x in a:
        tong += x
        if tong - k in dem:
            ket_qua += dem[tong - k]
        dem[tong] = dem.get(tong, 0) + 1
    return ket_qua


# Câu 46: Dãy số nguyên liên tiếp dài nhất (dùng tập băm)
def day_lien_tiep_dai_nhat(a):
    tap = set(a)
    dai_nhat = 0
    for x in tap:
        if x - 1 not in tap:            # x là điểm bắt đầu của 1 dãy
            y = x
            do_dai = 1
            while y + 1 in tap:
                y += 1
                do_dai += 1
            dai_nhat = max(dai_nhat, do_dai)
    return dai_nhat


# =====================================================================
# PHẦN 9 - HÀM BĂM (HASH FUNCTION) (Câu 47 - 50)
# =====================================================================

# Câu 47: Polynomial rolling hash
def polynomial_hash(s, p=31, m=10 ** 9 + 7):
    h = 0
    p_pow = 1
    for c in s:
        h = (h + (ord(c) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return h
    # p nên là số nguyên tố xấp xỉ kích thước bộ chữ cái (vd 31 cho chữ thường)
    # để phân bố hash đều hơn. m là số nguyên tố lớn để giảm khả năng đụng độ (va chạm mod).


# Câu 48: Rabin-Karp - tìm chuỗi mẫu bằng rolling hash
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return -1
    base = 256
    mod = 10 ** 9 + 7
    h_mul = 1                       # base^(m-1) % mod
    for _ in range(m - 1):
        h_mul = (h_mul * base) % mod

    h_pattern = 0
    h_text = 0
    for i in range(m):
        h_pattern = (h_pattern * base + ord(pattern[i])) % mod
        h_text = (h_text * base + ord(text[i])) % mod

    for i in range(n - m + 1):
        if h_pattern == h_text and text[i:i + m] == pattern:
            return i
        if i < n - m:
            # cập nhật hash cửa sổ trong O(1): bỏ ký tự đầu, thêm ký tự mới
            h_text = ((h_text - ord(text[i]) * h_mul) * base + ord(text[i + m])) % mod
    return -1


# Câu 49: Universal hashing
class UniversalHash:
    def __init__(self, m, p=(1 << 61) - 1):
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m
    # a, b được chọn NGẪU NHIÊN mỗi lần khởi tạo (không cố định),
    # nên kẻ tấn công không thể biết trước hàm băm để cố tình tạo ra
    # tập dữ liệu toàn bộ đụng độ vào cùng 1 bucket (tấn công từ chối dịch vụ qua hash).


# Câu 50: Bloom filter
class BloomFilter:
    def __init__(self, size=100, so_ham_bam=3):
        self.size = size
        self.so_ham_bam = so_ham_bam
        self.bit_array = [0] * size

    def _hash(self, item, seed):
        return hash((item, seed)) % self.size

    def add(self, item):
        for seed in range(self.so_ham_bam):
            idx = self._hash(item, seed)
            self.bit_array[idx] = 1

    def kiem_tra(self, item):
        for seed in range(self.so_ham_bam):
            idx = self._hash(item, seed)
            if self.bit_array[idx] == 0:
                return False        # chắc chắn KHÔNG có (không âm tính giả)
        return True                  # CÓ THỂ có (có thể là dương tính giả)
    # Xác suất dương tính giả tăng khi: số phần tử đã thêm càng nhiều,
    # bit_array càng nhỏ, hoặc số hàm băm không được chọn tối ưu.


# =====================================================================
# KHU VỰC TEST - chạy thử với các ví dụ trong đề bài
# =====================================================================
if __name__ == "__main__":
    print("--- PHẦN 1: TÌM KIẾM NHỊ PHÂN ---")
    print("Câu 1:", tim_kiem_nhi_phan([1, 3, 5, 7, 9], 7))                  # 3
    print("Câu 2:", dem_so_lan_xuat_hien([1, 2, 2, 2, 3], 2),
          tim_vi_tri_dau([1, 2, 2, 2, 3], 2), tim_vi_tri_cuoi([1, 2, 2, 2, 3], 2))
    print("Câu 3:", lower_bound([1, 3, 5, 7], 4))                          # 2
    print("Câu 4:", tim_kiem_mang_xoay([4, 5, 6, 7, 0, 1, 2], 0))           # 4
    print("Câu 5:", koko_an_chuoi([3, 6, 7, 11], 8))                       # 4
    print("Câu 6:", chia_mang_nho_nhat([7, 2, 5, 10, 8], 2))                # 18

    print("\n--- PHẦN 2: SẮP XẾP ---")
    print("Câu 7:", bubble_sort([2, 3, 1]))                                 # 2 swap
    print("Câu 8:", bubble_sort_toi_uu([1, 2, 3, 4]))                       # 1 lượt
    print("Câu 9:", insertion_sort([3, 2, 1]))                              # 3 shift
    print("Câu 10:", binary_insertion_sort([3, 2, 1]))
    print("Câu 11:", selection_sort([5, 4, 3, 2, 1])[1])                    # 10 so sánh
    print("Câu 12:", vi_du_selection_khong_on_dinh())
    print("Câu 13:", dem_nghich_the([2, 3, 1]))                             # 2
    print("Câu 14:", shell_sort([9, 8, 3, 7, 5, 6, 4, 1]))

    print("\n--- PHẦN 3: ĐỒ THỊ & DIJKSTRA ---")
    ke = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5)], [(4, 3)], []]
    print("Câu 15:", dijkstra(5, ke, 0))
    dist, parent = dijkstra_truy_vet(5, ke, 0)
    print("Câu 16:", in_duong_di(parent, 0, 4))
    print("Câu 18:", bellman_ford(5, [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (3, 4, 3)], 0))
    print("Câu 19:", duong_di_luoi([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))       # 7

    print("\n--- PHẦN 4: STACK ---")
    print("Câu 21:", dau_ngoac_can_bang("([]{})"), dau_ngoac_can_bang("([)]"))
    ms = MinStack()
    for v in [5, 3, 7]:
        ms.push(v)
    print("Câu 22:", ms.get_min())                                          # 3
    print("Câu 23:", tinh_hau_to("3 4 + 2 *"))                              # 14
    print("Câu 24:", next_greater_element([2, 1, 3]))                       # [3,3,-1]
    print("Câu 25:", histogram_lon_nhat([2, 1, 5, 6, 2, 3]))                # 10

    print("\n--- PHẦN 5: QUEUE ---")
    print("Câu 29:", max_cua_so_truot([1, 3, -1, -3, 5, 3], 3))             # [3,3,5,5]
    print("Câu 30:", round_robin([("P1", 5), ("P2", 4)], 2))

    print("\n--- PHẦN 6: ARRAY LIST ---")
    print("Câu 33:", xoay_mang([1, 2, 3, 4, 5], 2))                        # [4,5,1,2,3]
    print("Câu 34:", loai_trung_lap_On([3, 1, 3, 2, 1]))                   # [3,1,2]
    print("Câu 35:", merge_intervals([[1, 3], [2, 6], [8, 10]]))           # [[1,6],[8,10]]

    print("\n--- PHẦN 7: LINKED LIST ---")
    ll = tao_linked_list([1, 2, 3])
    print("Câu 36:", in_linked_list(dao_nguoc_lap(ll)))                    # [3,2,1]
    ll2 = tao_linked_list([1, 2, 3, 4, 5])
    print("Câu 37:", tim_nut_giua(ll2).val)                                # 3
    ll3 = tao_linked_list([1, 2, 3, 4, 5])
    print("Câu 39:", in_linked_list(xoa_nut_thu_k_tu_cuoi(ll3, 2)))         # [1,2,3,5]
    ll4 = tao_linked_list([3, 1, 2])
    print("Câu 40:", in_linked_list(sap_xep_linked_list(ll4)))             # [1,2,3]
    lru = LRUCache(2)
    lru.put(1, 'a'); lru.put(2, 'b'); lru.get(1); lru.put(3, 'c')
    print("Câu 41:", list(lru.data.items()))

    print("\n--- PHẦN 8: HASH TABLE ---")
    print("Câu 44:", two_sum([2, 7, 11], 9))                               # (0,1)
    print("Câu 45:", dem_doan_con_tong_bang_k([1, 1, 1], 2))                # 2
    print("Câu 46:", day_lien_tiep_dai_nhat([100, 4, 200, 1, 3, 2]))        # 4

    print("\n--- PHẦN 9: HASH FUNCTION ---")
    print("Câu 48:", rabin_karp("zabcd", "abc"))                           # 1
    bf = BloomFilter()
    bf.add("hello")
    print("Câu 50:", bf.kiem_tra("hello"), bf.kiem_tra("world"))