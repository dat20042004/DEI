# Phát biểu Bất biến vòng lặp (Loop Invariant):
# "Trước mỗi lần lặp của vòng lặp ngoài với chỉ số i, đoạn mảng con a[0..i-1] chứa i phần tử nhỏ nhất của toàn bộ mảng và đã được sắp xếp theo thứ tự tăng dần."
# 
# Chứng minh qua 3 bước:
# 1. Khởi tạo (Initialization): Trước khi i = 0, đoạn a[0..-1] rỗng -> Bất biến hiển nhiên đúng.
# 2. Duy trì (Maintenance): Ở vòng lặp i, ta tìm phần tử nhỏ nhất trong đoạn a[i..n-1] rồi hoán đổi về vị trí i. Do đoạn trước đó đã chứa các phần tử nhỏ nhất, phần tử mới thêm này chắc chắn lớn hơn hoặc bằng các phần tử trước đó và nhỏ hơn tất cả phần tử còn lại. Do đó đoạn a[0..i] tiếp tục chứa i+1 phần tử nhỏ nhất đúng thứ tự.
# 3. Hoàn thành (Termination): Thuật toán kết thúc khi i = n - 1. Khi đó, đoạn a[0..n-2] chứa n-1 phần tử nhỏ nhất đúng thứ tự. Phần tử cuối cùng a[n-1] hiển nhiên phải là phần tử lớn nhất. Vậy toàn bộ mảng đã được sắp xếp đúng.
print("Thuật toán Selection Sort hoàn toàn đúng đắn dựa trên bất biến vòng lặp.")