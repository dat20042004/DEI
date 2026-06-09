# Bài 25 - Bat bien vong lap (Loop Invariant) cua Bubble Sort
#
# Phat bieu:
#   Sau luot thu i (i bat dau tu 1),
#   i phan tu lon nhat da nam dung vi tri o cuoi mang.
#
# Chung minh:
#   - Luot 1: duyet tu j=0 den n-2, moi lan so sanh cap lien ke.
#     Phan tu lon nhat se duoc day dan den vi tri cuoi (a[n-1]).
#   - Luot 2: phan tu lon nhat thu 2 ve dung vi tri a[n-2].
#   - ...Tiep tuc den luot n-1.
#   => Sau n-1 luot, toan bo mang da sap xep dung.
#
# Thuat toan luon dung va dung lai vi:
#   - Moi luot giam pha can xu ly di 1 phan tu.
#   - Sau toi da n-1 luot, mang duoc sap xep hoan toan.

