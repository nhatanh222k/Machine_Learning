import numpy as np

# Trọng số w
w = np.array([1, 2, -10])

# Điểm dữ liệu x đã thêm bias
x = np.array([3, 4, 1])

# Nhãn thực tế
y = -1
# 1. Tính w^T * x


tich_vo_huong = np.dot(w, x)

print("1. Giá trị w^T*x =", tich_vo_huong)

# 2. Xác định nhãn dự đoán

if tich_vo_huong >= 0:
    y_du_doan = 1
else:
    y_du_doan = -1

print("2. Nhãn dự đoán =", y_du_doan)

# 3. Kiểm tra phân lớp đúng hay sai

if y_du_doan == y:
    print("3. Điểm dữ liệu được phân lớp đúng")
else:
    print("3. Điểm dữ liệu bị phân lớp sai")