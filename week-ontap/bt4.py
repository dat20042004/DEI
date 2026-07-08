
"""
CÂU 4 - Ứng dụng Ngăn xếp (Stack đơn điệu)

Đề bài: T = [73,74,75,71,69,72,76,73]. Đếm số ngày ít nhất phải chờ để
có 1 ngày ấm hơn cho mỗi ngày. Nếu không có, trả về 0.
"""

# Ý tưởng: dùng stack lưu CHỈ SỐ của những ngày mà chưa tìm được ngày ấm
# hơn phía sau. Duyệt từng ngày i: trong khi nhiệt độ hôm nay > nhiệt độ
# của ngày ở đỉnh stack, ta biết ngày ở đỉnh stack đã tìm được câu trả lời
# (khoảng cách = i - đỉnh_stack) -> pop ra và ghi kết quả, rồi đẩy i vào.

def so_ngay_cho_am_hon(t):
    n = len(t)
    ket_qua = [0] * n
    ngan_xep = []          # lưu chỉ số ngày, nhiệt độ giảm dần từ đáy lên đỉnh
    for i in range(n):
        while ngan_xep and t[ngan_xep[-1]] < t[i]:
            idx = ngan_xep.pop()
            ket_qua[idx] = i - idx
        ngan_xep.append(i)
    return ket_qua


if __name__ == "__main__":
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    ket_qua = so_ngay_cho_am_hon(t)

    print("Nhiệt độ =", t)
    print("Kết quả  =", ket_qua)