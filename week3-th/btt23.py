def phan_tich(a):
    so_ss = 0
    so_swap = 0
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            so_ss += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                so_swap += 1
    return so_ss, so_swap

ngau_nhien = [4, 2, 7, 1, 3]
da_sap_xep = [1, 2, 3, 4, 5]
nguoc = [5, 4, 3, 2, 1]

ss1, sw1 = phan_tich(ngau_nhien[:])
ss2, sw2 = phan_tich(da_sap_xep[:])
ss3, sw3 = phan_tich(nguoc[:])

print(f"Ngau nhien: so sanh={ss1}, swap={sw1}")
print(f"Da sap xep: so sanh={ss2}, swap={sw2}")
print(f"Sap xep nguoc: so sanh={ss3}, swap={sw3}")