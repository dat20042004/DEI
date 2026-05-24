""" Bài 18. Tìm kiếm trên ma trận 2 chiều
Cho ma trận (mảng 2 chiều) các số nguyên. Viết hàm tìm kiếm tuyến tính giá trị x trong ma
trận, trả về vị trí (dòng, cột) đầu tiên tìm thấy, hoặc (-1, -1) nếu không có"""
def tim_trong_ma_tran(M, x):
    so_dong = len(M)
    so_cot = len(M[0])
    
    for dòng in range(so_dong):
        for cột in range(so_cot):
            if M[dòng][cột] == x:
                return (dòng, cột)  # Thấy thì trả về tọa độ (dòng, cột) [cite: 86]
                
    return (-1, -1)  # Không thấy 