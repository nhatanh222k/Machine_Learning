import numpy #thu vien xu ly mang
from sklearn.model_selection import cross_val_score #thu vien chia tap du lieu
from sklearn.preprocessing import PolynomialFeatures #thu vien chuyen doi du lieu sang dang da thuc(hỗ trọ ví dụ overfitting)
from sklearn.linear_model import LinearRegression #thu vien hoi quy tuyen tinh
from sklearn.pipeline import make_pipeline #thu vien tao pipeline cho cac buoc xu ly du lieu
X = numpy.array([
    [40, 50, 60, 70, 80, 90, 100, 110, 120, 130],#dien tich
    [2,  2,  2,  3,  3,  3,   4,   4,   4,   5],#So phong
    [10, 8,  9,  7, 6,  5,   7,   4,   3,   2] #cach trung tam
])
Y=numpy.array([[8],
    [10],
    [11],
    [14],
    [15],
    [17],
    [19],
    [22],
    [24],
    [27]]) #gia nha
X = X.T
# LẦN 1: Dùng BẬC 3 (Mô hình quá phức tạp -> BỊ OVERFITTING)
# Tạo mô hình hồi quy đa thức bậc 3
# PolynomialFeatures(degree=3): chuyển X thành các đặc trưng đa thức bậc 3
# LinearRegression(): dùng hồi quy tuyến tính để học từ các đặc trưng đó
# make_pipeline(): kết hợp 2 bước trên thành một mô hình
mo_hinh_bac_3 = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
# Cho mô hình bậc 3 học từ dữ liệu X và giá nhà Y
mo_hinh_bac_3.fit(X, Y)
# Tính điểm của mô hình trên chính dữ liệu mà nó đã học
print("Điểm học thuộc lòng (Bậc 3):", mo_hinh_bac_3.score(X, Y))
diem_cv_bac_3 = cross_val_score(mo_hinh_bac_3, X, Y, cv=5)
# Tính điểm CV trung bình của 5 lần đánh giá
# Điểm CV thấp hoặc âm cho thấy mô hình dự đoán dữ liệu mới kém
print("Điểm CV thực tế (Bậc 3):    ", diem_cv_bac_3.mean())
# LẦN 2: Dùng BẬC 1 (Mô hình đơn giản -> SỬA OVERFITTING)
# Tạo mô hình hồi quy đa thức bậc 1
# degree=1: chỉ sử dụng các đặc trưng bậc 1
# Mô hình đơn giản hơn so với bậc 3
mo_hinh_bac_1 = make_pipeline(PolynomialFeatures(degree=1), LinearRegression())
# Đánh giá mô hình bậc 1 bằng Cross Validation 5 lần
# Không cần fit() trước vì cross_val_score() sẽ tự chia dữ liệu,
# tự huấn luyện và tự kiểm tra mô hình trong từng lần
diem_cv_bac_1 = cross_val_score(mo_hinh_bac_1, X, Y, cv=5)
print("\nĐiểm CV thực tế (Bậc 1):    ", diem_cv_bac_1.mean())
