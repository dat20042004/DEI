def explain_dijkstra_correctness():
    proof = """
    ===========================================================================
    CHỨNG MINH TÍNH ĐÚNG ĐẮN CỦA THUẬT TOÁN DIJKSTRA (BẰNG PHẢN CHỨNG)
    ===========================================================================
    
    Phát biểu định lý (Bất biến tham lam):
    Khi một đỉnh 'u' được chọn để chốt (lấy ra khỏi hàng đợi ưu tiên), thì giá trị 
    khoảng cách tạm thời dist[u] tại thời điểm đó chính là khoảng cách ngắn nhất 
    thực tế từ đỉnh nguồn 's' tới 'u'.
    
    Chứng minh bằng phương pháp phản chứng:
    1. Giả sử tại một bước bất kỳ, thuật toán chọn chốt đỉnh 'u', nhưng dist[u] 
       chưa tối ưu. Có nghĩa là tồn tại một con đường bí mật khác ngắn hơn đi từ 
       's' qua tập các đỉnh đã chốt, rồi rẽ sang một đỉnh chưa chốt 'x', rồi mới 
       đi đến 'u'.
       
       Đường đi giả thuyết: s -> ... -> y (đã chốt) -> x (chưa chốt) -> ... -> u
       
    2. Vì đỉnh 'x' nằm ngay sau một đỉnh 'y' đã được chốt, thao tác nới lỏng 
       (Relaxation) từ 'y' chắc chắn đã được thực thi từ trước. Do đó:
       dist[x] chính là độ dài ngắn nhất từ s đến x.
       
    3. Vì mọi trọng số cạnh trên đồ thị đều không âm (w >= 0), việc đi thêm 
       các cạnh trung chuyển tiếp theo từ 'x' đến 'u' chắc chắn sẽ làm tăng hoặc 
       giữ nguyên tổng chiều dài quãng đường. Suy ra:
       dist[x] <= độ dài đường đi giả thuyết tới u < dist[u] (theo giả thuyết phản chứng).
       
    4. Từ chuỗi logic trên, ta suy ra được: dist[x] < dist[u].
       Điều này hoàn toàn MÂU THUẪN với nguyên lý tham lam của thuật toán Dijkstra 
       (Thuật toán luôn bắt buộc chọn đỉnh chưa chốt có dist nhỏ nhất, nếu dist[x] < dist[u] 
       thì thuật toán phải chọn chốt đỉnh 'x' trước chứ không phải đỉnh 'u').
       
    VÌ SAO CHỨNG MINH NÀY CẦN TRỌNG SỐ KHÔNG ÂM?
    Nếu đồ thị tồn tại cạnh có trọng số âm, lập luận ở mục (3) sẽ bị phá vỡ hoàn toàn. 
    Việc đi tiếp từ 'x' qua các cạnh âm hoàn toàn có thể làm giảm tổng chiều dài con 
    đường xuống mức nhỏ hơn cả dist[x], khiến giả định dist[x] <= dist[u] sai bản chất. 
    Dijkstra sẽ chốt sai và không thể tự quay đầu sửa lỗi.
    """
    print(proof)

if __name__ == "__main__":
    explain_dijkstra_correctness()