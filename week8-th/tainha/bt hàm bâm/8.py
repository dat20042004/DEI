def quadratic_probe_put(table, key, size):
    idx = hash(key) % size
    buoc = 1
    # Tìm ô trống bằng bước nhảy bình phương
    while table[idx] is not None:
        idx = (idx + buoc**2) % size
        buoc += 1
    table[idx] = key