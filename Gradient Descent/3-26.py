# Hàm số
def f(x):
    return x**2 - 4*x + 5

# Đạo hàm của hàm số
def dao_ham(x):
    return 2*x - 4

# Giá trị ban đầu
x = 5

# Learning rate
eta = 0.2

# In đạo hàm
print("Đạo hàm: f'(x) = 2x - 4")
print()

# Thực hiện 4 bước Gradient Descent
for i in range(4):
    print("Bước", i)
    print("x =", x)
    print("f(x) =", f(x))
    print("f'(x) =", dao_ham(x))

    # Công thức Gradient Descent
    x = x - eta * dao_ham(x)

    print("x mới =", x)
    print("--------------------")

# In kết quả cuối cùng
print("Sau 4 bước:")
print("x =", x)
print("f(x) =", f(x))