import numpy as np
# Hàm đạo hàm của f(x) = x^2 - 2
def grad(x):
    return 2*x
# Hàm f(x)
def cost(x):
    return x**2 - 2
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
x0 = 5
eta = 0.1
x, it = myGD(x0, eta)
print("Các giá trị x:", x)
print("Giá trị cực tiểu x =", x[-1])
print("Giá trị nhỏ nhất f(x) =", cost(x[-1]))
print("Số lần lặp =", it)