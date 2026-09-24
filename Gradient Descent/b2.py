import numpy as np
# Hàm đạo hàm của g(x) = (1/3)x^3 - x
def grad(x):
    return x**2 - 1
# Hàm g(x)
def cost(x):
    return (1/3)*x**3 - x
# Gradient Descent
def myGD(x0, eta):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta * grad(x[-1])
        if abs(x_new - x[-1]) <= 1e-3:
            break
        x.append(x_new)
    return x, it
# Giá trị ban đầu
x0 = 0
eta = 0.1
x, it = myGD(x0, eta)
print("Các giá trị x:", x)
print("Giá trị cực tiểu x =", x[-1])
print("Giá trị nhỏ nhất g(x) =", cost(x[-1]))
print("Số lần lặp =", it)