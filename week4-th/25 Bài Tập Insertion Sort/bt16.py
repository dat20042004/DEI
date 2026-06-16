class OnlineInsertionSort:
    def __init__(self):
        self.arr = []

    def add(self, x):
        self.arr.append(x)
        i = len(self.arr) - 2
        # Tương tự cấu trúc vòng lặp lõi của Insertion Sort
        while i >= 0 and self.arr[i] > x:
            self.arr[i + 1] = self.arr[i]
            i -= 1
        self.arr[i + 1] = x
        print(self.arr)

stream = [5, 2, 8, 1]
online_sort = OnlineInsertionSort()
for val in stream:
    online_sort.add(val)
# In ra lần lượt luồng dữ liệu liên tục: [5] -> [2, 5] -> [2, 5, 8] -> [1, 2, 5, 8]