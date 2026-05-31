# Bai 22: Tim trung vi cua hai mang da sap xep
def trung_vi(a, b):
    # Dam bao a la mang ngan hon
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    trai, phai = 0, m
    while trai <= phai:
        chia_a = (trai + phai) // 2
        chia_b = (m + n + 1) // 2 - chia_a
        # Lay gia tri bien cua hai phan
        trai_a = a[chia_a - 1] if chia_a > 0 else float('-inf')
        phai_a = a[chia_a]     if chia_a < m else float('inf')
        trai_b = b[chia_b - 1] if chia_b > 0 else float('-inf')
        phai_b = b[chia_b]     if chia_b < n else float('inf')
        if trai_a <= phai_b and trai_b <= phai_a:
            if (m + n) % 2 == 1:
                return float(max(trai_a, trai_b))
            else:
                return (max(trai_a, trai_b) + min(phai_a, phai_b)) / 2.0
        elif trai_a > phai_b:
            phai = chia_a - 1
        else:
            trai = chia_a + 1

a = [1, 3]
b = [2]
print("Trung vi:", trung_vi(a, b))

a2 = [1, 2]
b2 = [3, 4]
print("Trung vi:", trung_vi(a2, b2))