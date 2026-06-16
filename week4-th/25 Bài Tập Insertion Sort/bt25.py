Phát biểu bất biến vòng lặp (Loop Invariant):
"Tại thời điểm bắt đầu mỗi vòng lặp ngoài của biến chỉ số i, mảng con gồm các phần tử a[0..i-1] chính là tập hợp các phần tử ban đầu thuộc các vị trí từ 0 đến i-1 nhưng đã được sắp xếp hoàn chỉnh theo thứ tự tăng dần."

Chứng minh:
1. Khởi tạo (Initialization): Trước vòng lặp đầu tiên (i = 1), mảng con chỉ chứa duy nhất một phần tử a[0]. Một mảng có 1 phần tử thì hiển nhiên luôn luôn đúng cấu trúc đã sắp xếp.
2. Duy trì (Maintenance): Ở vòng lặp thứ i, thuật toán tiến hành lấy giá trị key = a[i] dịch chuyển ngược về bên trái, đẩy các phần tử lớn hơn nó sang phải để nhường chỗ. Vì đoạn trước đó a[0..i-1] đã sắp xếp, việc chèn thêm một phần tử vào đúng quy luật giúp mảng con mở rộng a[0..i] tiếp tục duy trì trạng thái sắp xếp tăng dần.
3. Hoàn thành (Termination): Vòng lặp kết thúc khi chỉ số i = n. Thay thế vào phát biểu bất biến, ta thu được đoạn mảng con a[0..n-1] (tức là toàn bộ mảng đầu vào) gồm các phần tử ban đầu đã được sắp xếp tăng dần một cách chính xác. Thuật toán đúng.