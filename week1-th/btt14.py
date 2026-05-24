'''Bài 14. Tìm theo điều kiện
Viết hàm tìm số chẵn đầu tiên trong mảng và trả về vị trí của nó. Nếu mảng không có số
chẵn nào, trả về -1     '''
def tim_so_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:  # Thỏa mãn điều kiện số chẵn
            return i       # Trả về vị trí ngay lập tức
    return -1