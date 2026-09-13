from sklearn.linear_model import LinearRegression
X = [[20], [30], [40], [50], [60]]
y = [500, 700, 900, 1100, 1300]
model = LinearRegression()
model.fit(X, y)
dien_tich = float(input("Nhap dien tich nha: "))
gia = model.predict([[dien_tich]])

print("Gia nha du doan:", gia[0], "trieu")