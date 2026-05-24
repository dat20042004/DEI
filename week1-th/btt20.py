'''Bài 20. Bài toán tổng hợp — Quản lý danh bạ
Viết chương trình quản lý danh bạ điện thoại đơn giản, sử dụng tìm kiếm tuyến tính cho các
chức năng: (1) thêm liên hệ gồm tên và số điện thoại; (2) tìm số điện thoại theo tên; (3) tìm
tên theo số điện thoại; (4) đếm số liên hệ có số điện thoại bắt đầu bằng một đầu số cho trước
(ví dụ "090"). Thiết kế menu lặp lại cho người dùng chọn chức năng'''
danh_ba = []  # Nơi lưu trữ các liên hệ, mỗi liên hệ là một dict {"ten": ..., "sdt": ...} [cite: 95]

while True:
    print("\n--- MENU QUẢN LÝ DANH BẠ ---") 
    print("1. Thêm liên hệ") 
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại") 
    print("4. Đếm đầu số máy") 
    print("5. Thoát")
    
    luon_chon = input("Mời bạn chọn chức năng (1-5): ")
    
    if luon_chon == "1":
        ten = input("Nhập tên: ")
        sdt = input("Nhập SĐT: ")
        danh_ba.append({"ten": ten, "sdt": sdt}) 
        print("Đã thêm thành công!")
        
    elif luon_chon == "2":
        ten_tim = input("Nhập tên cần tìm: ")
        found = False
        for liên_hệ in danh_ba:
            if liên_hệ["ten"].lower() == ten_tim.lower():
                print("SĐT của bạn đó là:", liên_hệ["sdt"]) 
                found = True
                break
        if not found:
            print("Không tìm thấy tên này.")
            
    elif luon_chon == "3":
        sdt_tim = input("Nhập SĐT cần tìm: ")
        found = False
        for liên_hệ in danh_ba:
            if liên_hệ["sdt"] == sdt_tim:
                print("Tên của chủ số điện thoại:", liên_hệ["ten"]) 
                found = True
                break
        if not found:
            print("Không tìm thấy số điện thoại này.")
            
    elif luon_chon == "4":
        dau_so = input("Nhập đầu số cần đếm (ví dụ 090): ") 
        dem = 0
        for liên_hệ in danh_ba:
            # .startswith() dùng để kiểm tra xem chuỗi có bắt đầu bằng cụm từ đó không
            if liên_hệ["sdt"].startswith(dau_so): 
                dem += 1
        print(f"Có {dem} liên hệ sử dụng đầu số {dau_so}") 
        
    elif luon_chon == "5":
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")