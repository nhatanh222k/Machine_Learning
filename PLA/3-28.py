import numpy as np

# Trọng số ban đầu
w = np.array([-2, 1, 0])

# Điểm dữ liệu đã thêm bias
x = np.array([2, 3, 1])

# Nhãn thực tế
y = 1

# Learning rate của Perceptron
eta = 1

# 1. Kiểm tra mẫu có bị phân lớp sai

# Tính w^T * x
gia_tri = np.dot(w, x)

print("w^T*x ban đầu =", gia_tri)

# Kiểm tra phân lớp sai
# Mẫu bị sai khi y * (w^T*x) <= 0
if y * gia_tri <= 0:
    print("Mẫu bị phân lớp sai")

    # 2. Cập nhật Perceptron

    w = w + eta * y * x

    print("w sau khi cập nhật =", w)

else:
    print("Mẫu được phân lớp đúng")

# 3. Tính lại w^T*x sau cập nhật

gia_tri_moi = np.dot(w, x)

print("w^T*x sau cập nhật =", gia_tri_moi)