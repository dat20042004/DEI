'''Bài 12. Min và Max trong một lần duyệt
Chỉ với một lần duyệt mảng, hãy tìm đồng thời giá trị nhỏ nhất và giá trị lớn nhất, đồng thời
in ra vị trí tương ứng của chúng.'''
def tim_min_max(a):
    if len(a) == 0:
        return None, -1, None, -1
        
    g_min = g_max = a[0]  # Khởi tạo giá trị ban đầu là phần tử đầu tiên
    v_min = v_max = 0
    
    for i in range(1, len(a)):
        if a[i] > g_max:
            g_max = a[i]
            v_max = i
        if a[i] < g_min:  # Tiện tay kiểm tra luôn xem nó có nhỏ nhất không
            g_min = a[i]
            v_min = i
            
    return g_min, v_min, g_max, v_max