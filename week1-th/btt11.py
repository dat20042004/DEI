''' Bài 11. Tìm giá trị lớn nhất
Không dùng hàm max() có sẵn, hãy dùng kỹ thuật duyệt tuyến tính để tìm giá trị lớn nhất
và vị trí của nó trong mảng.'''
def tim_max(a):
    if len(a) == 0:
        return None, -1  # Mảng rỗng thì không có max
        
    giatri_max = a[0]  # Tạm thời giả định đứa đầu tiên là lớn nhất
    vitri_max = 0
    
    for i in range(1, len(a)):
        if a[i] > giatri_max:  # Nếu gặp đứa khác to hơn vị vua hiện tại
            giatri_max = a[i]  # Phong chức vua mới cho nó
            vitri_max = i      # Ghi lại vị trí của vua mới
            
    return giatri_max, vitri_max