import numpy as np

# XÂY DỰNG LỚP PERCEPTRON

class Perceptron:

    # Hàm khởi tạo
    def __init__(self, learning_rate=1, so_vong_lap=10):
        self.learning_rate = learning_rate
        self.so_vong_lap = so_vong_lap
        self.w = None

    # Hàm fit: huấn luyện mô hình

    def fit(self, X, y):

        # Khởi tạo trọng số bằng 0
        self.w = np.zeros(X.shape[1])

        # Lặp nhiều lần để huấn luyện
        for vong in range(self.so_vong_lap):

            # Duyệt từng điểm dữ liệu
            for i in range(len(X)):

                # Tính w^T * x
                gia_tri = np.dot(self.w, X[i])

                # Dự đoán nhãn
                if gia_tri >= 0:
                    y_du_doan = 1
                else:
                    y_du_doan = -1

                # Nếu dự đoán sai thì cập nhật w
                if y_du_doan != y[i]:
                    self.w = self.w + self.learning_rate * y[i] * X[i]

        return self

    # Hàm predict: dự đoán dữ liệu mới
    def predict(self, X):

        ket_qua = []

        # Duyệt từng điểm dữ liệu
        for x in X:

            # Tính w^T * x
            gia_tri = np.dot(self.w, x)

            # Xác định nhãn
            if gia_tri >= 0:
                ket_qua.append(1)
            else:
                ket_qua.append(-1)

        return np.array(ket_qua)

# DỮ LIỆU HUẤN LUYỆN

# X đã thêm bias
X = np.array([
    [1, 2, 3],
    [1, 3, 4],
    [1, 4, 5],
    [1, -2, -3],
    [1, -3, -4],
    [1, -4, -5]
])

# Nhãn
y = np.array([1, 1, 1, -1, -1, -1])

# TẠO VÀ HUẤN LUYỆN MÔ HÌNH

mo_hinh = Perceptron(learning_rate=1, so_vong_lap=10)

mo_hinh.fit(X, y)

print("Trọng số sau khi huấn luyện:")
print(mo_hinh.w)

# DỰ ĐOÁN DỮ LIỆU MỚI

X_moi = np.array([
    [1, 5, 6],
    [1, -5, -6]
])

du_doan = mo_hinh.predict(X_moi)

print("Nhãn dự đoán:")
print(du_doan)