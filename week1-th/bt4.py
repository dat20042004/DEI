'''
Phần A HIểu thuật toán 
bài 1 Trình bài ý tưởng 
Ý tưởng chính:  
Thuật toán tìm kiếm tuyến tính duyệt qua từng phần tử của mảng (hoặc danh sách) từ đầu đến cuối, so sánh lần lượt với giá trị cần tìm. Nếu tìm thấy phần tử bằng giá trị cần tìm thì trả về vị trí của nó; nếu duyệt hết mà không thấy thì kết luận là không tồn tại.

Input (đầu vào):

Một mảng (hoặc danh sách) các phần tử.

Giá trị cần tìm 
𝑥
.

Output (đầu ra):

Vị trí (chỉ số) của phần tử 
𝑥
 trong mảng nếu tồn tại.

Nếu không tồn tại, trả về giá trị đặc biệt (ví dụ: -1 hoặc thông báo “không tìm thấy”).

Điều kiện dừng:

Khi tìm thấy phần tử bằng giá trị cần tìm → thuật toán dừng ngay và trả về vị trí.

Khi đã duyệt hết toàn bộ mảng mà không tìm thấy → thuật toán dừng và trả về -1.
'''
'''Bai 2 Mô phỏng số phép so sánh 
Cho mảng A = [7, 3, 9, 12, 5, 8, 1] và x = 5. Hãy lập bảng mô phỏng từng bước: ở mỗi bước
ghi rõ chỉ số i, giá trị A[i], kết quả so sánh A[i] với x, và kết luận. Cuối cùng cho biết giá trị mà
hàm trả về
| Bước | i | A[i] | So sánh A[i] với x | Kết luận |
| --- | --- | --- | --- | --- |
| 1 | 0 | 7 | 7 ≠ 5 | Chưa tìm thấy, tiếp tục |
| 2 | 1 | 3 | 3 ≠ 5 | Chưa tìm thấy, tiếp tục |
| 3 | 2 | 9 | 9 ≠ 5 | Chưa tìm thấy, tiếp tục |
| 4 | 3 | 12 | 12 ≠ 5 | Chưa tìm thấy, tiếp tục |
| 5 | 4 | 5 | 5 = 5 | **Tìm thấy tại vị trí i = 4, dừng** |

'''
""" Bài 4. Phân tích độ phức tạp
Một mảng có n phần tử. Hãy cho biết số phép so sánh trong: (a) trường hợp tốt nhất;  (b)
trường hợp xấu nhất;  (c) trung bình (khi phần tử có trong mảng). Từ đó suy ra độ phức tạp
thời gian của thuật toán theo ký hiệu O lớn
Giả sử mảng có n phần tử và ta cần tìm giá trị 
𝑥
:

Trường hợp tốt nhất (best case):

Phần tử cần tìm nằm ngay ở vị trí đầu tiên (i = 0).

Số phép so sánh = 1.

Độ phức tạp thời gian: 
𝑂(1)
.

Trường hợp xấu nhất (worst case):

Phần tử cần tìm nằm ở cuối mảng hoặc không tồn tại trong mảng.

Số phép so sánh = n.

Độ phức tạp thời gian: 
𝑂(𝑛)
.

Trường hợp trung bình (average case – giả sử phần tử có trong mảng):

Xác suất tìm thấy ở mỗi vị trí là như nhau.

Trung bình sẽ phải duyệt khoảng n/2 phần tử.

Số phép so sánh ≈ n/2.

Độ phức tạp thời gian: 
𝑂(𝑛)
.

 Kết luận
Trong mọi trường hợp, độ phức tạp thời gian của thuật toán tìm kiếm tuyến tính được biểu diễn bằng ký hiệu O(n).

Tuy nhiên, ta có thể phân biệt rõ:

Tốt nhất: 
𝑂(1)

Trung bình: 
𝑂(𝑛)

Xấu nhất: 
𝑂(𝑛)
"""
"""Bài 5. Điều kiện áp dụng
Tìm kiếm tuyến tính có bắt buộc mảng phải được sắp xếp trước hay không? Giải thích. So
sánh ngắn gọn với tìm kiếm nhị phân về: điều kiện áp dụng và độ phức tạp
Có cần sắp xếp mảng trước không?  
→ Không bắt buộc.  
Thuật toán tìm kiếm tuyến tính chỉ đơn giản duyệt tuần tự từng phần tử và so sánh với giá trị cần tìm. Vì vậy, nó hoạt động được trên cả mảng chưa sắp xếp lẫn đã sắp xếp.

Giải thích:

Ưu điểm: dễ cài đặt, không yêu cầu dữ liệu có cấu trúc đặc biệt.

Nhược điểm: tốc độ chậm khi mảng lớn, vì phải duyệt nhiều phần tử.
| Tiêu chí | Tìm kiếm tuyến tính | Tìm kiếm nhị phân |
| --- | --- | --- |
| **Điều kiện áp dụng** | Không cần mảng sắp xếp | Bắt buộc mảng **đã sắp xếp** |
| **Độ phức tạp tốt nhất** | O(1) (phần tử ở đầu) | O(1) (phần tử ở giữa) |
| **Độ phức tạp trung bình** | O(n) | O(log n) |
| **Độ phức tạp xấu nhất** | O(n) | O(log n) |
| **Ưu điểm** | Đơn giản, áp dụng mọi loại dữ liệu | Nhanh hơn nhiều khi dữ liệu lớn |
| **Nhược điểm** | Chậm với mảng lớn | Không dùng được nếu dữ liệu chưa sắp xếp |Kết luận:

Tìm kiếm tuyến tính phù hợp khi dữ liệu nhỏ hoặc chưa sắp xếp.

Tìm kiếm nhị phân hiệu quả hơn nhiều nhưng chỉ dùng được khi dữ liệu đã sắp xếp.

"""

