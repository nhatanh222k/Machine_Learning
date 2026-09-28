import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# 1. DỮ LIỆU GIAO DỊCH

# Các đặc trưng:
# x1: Số tiền giao dịch
# x2: Số lần giao dịch trong ngày
# x3: Khoảng cách từ vị trí giao dịch đến vị trí thường dùng

X = np.array([
    [100, 2, 5],
    [150, 3, 8],
    [200, 2, 10],
    [250, 4, 7],
    [300, 3, 6],
    [350, 5, 9],
    [400, 4, 12],
    [450, 5, 15],
    [500, 6, 20],
    [550, 5, 18],

    [1000, 15, 500],
    [1200, 20, 600],
    [1500, 18, 700],
    [2000, 25, 800],
    [2500, 30, 900],
    [3000, 35, 1000],
    [3500, 40, 1200],
    [4000, 45, 1500],
    [4500, 50, 1800],
    [5000, 55, 2000]
])


# Nhãn:
# 0 = giao dịch bình thường
# 1 = giao dịch gian lận

y = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,

    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1
])

# 2. CHIA DỮ LIỆU TRAIN VÀ TEST

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# 3. CHUẨN HÓA DỮ LIỆU

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# 4. XÂY DỰNG MÔ HÌNH PERCEPTRON

mo_hinh = Perceptron(
    max_iter=1000,
    eta0=0.1,
    random_state=42
)

# 5. HUẤN LUYỆN

mo_hinh.fit(X_train, y_train)

# 6. DỰ ĐOÁN

y_du_doan = mo_hinh.predict(X_test)

# 7. TÍNH CÁC ĐỘ ĐO

accuracy = accuracy_score(y_test, y_du_doan)

precision = precision_score(y_test, y_du_doan)

recall = recall_score(y_test, y_du_doan)

f1 = f1_score(y_test, y_du_doan)

# 8. IN KẾT QUẢ

print("KẾT QUẢ MÔ HÌNH PERCEPTRON")
print("----------------------------")

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1-score :", f1)

print()
print("Ma trận nhầm lẫn:")
print(confusion_matrix(y_test, y_du_doan))