"""
    Yêu cầu người dùng nhập vào 3 số a, b, c
    Tìm nghiệm của phương trình bậc 2
    ax^2 + bx + c = 0
"""
from math import sqrt

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a == 0:
    if b == 0 and c == 0:
        print("Infinitely many solutions")
    elif b == 0 and c != 0:
        print("No solution")
    else:
        print("x =", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("No solution")
    elif delta == 0:
        x = -b / (2 * a)
        print("x1 = x2 =", x)
    else:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)
