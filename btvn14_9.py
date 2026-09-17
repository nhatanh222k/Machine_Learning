import numpy
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error


# ==========================================
# 1. DỮ LIỆU X VÀ Y
# ==========================================

X = numpy.array([
    [40, 50, 60, 70, 80, 90, 100, 110, 120, 130],
    [2,  2,  2,  3,  3,  3,   4,   4,   4,   5],
    [10, 8,  9,  7, 6,  5,   7,   4,   3,   2]
])

Y = numpy.array([
    [8],
    [10],
    [11],
    [14],
    [15],
    [17],
    [19],
    [22],
    [24],
    [27]
])

# Chuyển vị X
X = X.T


# ==========================================
# 2. DANH SÁCH BẬC MÔ HÌNH
# ==========================================

degrees = range(1, 6)


# ==========================================
# 3. K-FOLD CROSS VALIDATION
# ==========================================

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


train_errors = []
cv_errors = []


# ==========================================
# 4. THỬ TỪNG BẬC
# ==========================================

for degree in degrees:

    mo_hinh = make_pipeline(
        PolynomialFeatures(degree=degree),
        LinearRegression()
    )

    # -------------------------
    # TRAIN
    # -------------------------

    mo_hinh.fit(X, Y)

    Y_train_du_doan = mo_hinh.predict(X)

    train_error = mean_squared_error(
        Y,
        Y_train_du_doan
    )

    train_errors.append(train_error)


    # -------------------------
    # CROSS VALIDATION
    # -------------------------

    diem_cv = cross_val_score(
        mo_hinh,
        X,
        Y,
        cv=cv,
        scoring="neg_mean_squared_error"
    )

    cv_error = -diem_cv.mean()

    cv_errors.append(cv_error)


# ==========================================
# 5. TÌM BẬC TỐT NHẤT
# ==========================================

vi_tri = numpy.argmin(cv_errors)

bac_tot_nhat = list(degrees)[vi_tri]


# ==========================================
# 6. IN KẾT QUẢ
# ==========================================

print("===== KẾT QUẢ =====")

for i in range(len(degrees)):

    print(
        "Bậc", degrees[i],
        "| Train Error =", train_errors[i],
        "| CV Error =", cv_errors[i]
    )

print("\nBậc được chọn bằng K-fold CV:", bac_tot_nhat)


# ==========================================
# 7. VẼ ĐỒ THỊ
# ==========================================

plt.figure(figsize=(10, 6))


# Train Error
plt.plot(
    list(degrees),
    train_errors,
    marker="o",
    linewidth=2,
    label="Train error"
)


# Validation Error
plt.plot(
    list(degrees),
    cv_errors,
    marker="o",
    linewidth=2,
    label="Validation error (K-fold CV)"
)


# Đánh dấu bậc được CV chọn
plt.axvline(
    bac_tot_nhat,
    linestyle="--",
    linewidth=2,
    label=f"Bậc được CV chọn = {bac_tot_nhat}"
)


# ==========================================
# 8. GHI UNDERFITTING / OVERFITTING
# ==========================================

y_max = max(cv_errors)

plt.text(
    1.05,
    y_max * 0.85,
    "UNDERFITTING",
    fontsize=13
)

plt.text(
    3.2,
    y_max * 0.85,
    "OVERFITTING",
    fontsize=13
)


# ==========================================
# 9. TIÊU ĐỀ VÀ TRỤC
# ==========================================

plt.xlabel("Degree")
plt.ylabel("Mean Squared Error")

plt.title(
    "Phát hiện Overfitting bằng K-fold Cross Validation"
)

plt.xticks(list(degrees))

plt.legend()

plt.grid(True)


# ==========================================
# 10. LƯU ĐỒ THỊ
# ==========================================

plt.savefig(
    "do_thi_overfitting.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nĐã tạo file: do_thi_overfitting.png")