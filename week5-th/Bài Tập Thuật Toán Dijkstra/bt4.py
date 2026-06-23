def print_distances(dist):
    for i, d in enumerate(dist):
        if d == float('inf'):
            print(f"Đỉnh {i}: -1 (Không thể tới)")
        else:
            print(f"Đỉnh {i}: {d}")

if __name__ == "__main__":
    # Giả lập mảng kết quả thu được từ thuật toán
    sample_dist = [0, 3, 1, 4, 7, 9]
    print_distances(sample_dist)