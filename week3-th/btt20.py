def dem_nghich_the_nhanh(a):
    if len(a) <= 1:
        return a, 0
    giua = len(a) // 2
    trai, dem_trai = dem_nghich_the_nhanh(a[:giua])
    phai, dem_phai = dem_nghich_the_nhanh(a[giua:])
    ket_hop = []
    dem = dem_trai + dem_phai
    i = j = 0
    while i < len(trai) and j < len(phai):
        if trai[i] <= phai[j]:
            ket_hop.append(trai[i])
            i += 1
        else:
            ket_hop.append(phai[j])
            dem += len(trai) - i
            j += 1
    ket_hop += trai[i:]
    ket_hop += phai[j:]
    return ket_hop, dem

a = [2, 3, 1]
_, ket_qua = dem_nghich_the_nhanh(a)
print(ket_qua)