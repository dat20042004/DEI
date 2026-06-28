# Bài 3. Mô phỏng dãy thao tác
def simulate_stack_operations(operations):
    stack = []
    for op in operations:
        if op.startswith("push"):
            _, val = op.split()
            stack.append(int(val))
        elif op == "pop":
            if stack:
                print(f"pop in {stack.pop()}")
            else:
                print("pop lỗi: Stack rỗng")
    print(f"Trạng thái cuối cùng: {stack}")

# Ví dụ kiểm thử
if __name__ == "__main__":
    ops = ["push 5", "push 7", "pop"]
    simulate_stack_operations(ops)  # In: pop in 7 -> Trạng thái cuối cùng: [5]