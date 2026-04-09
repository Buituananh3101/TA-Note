"""
    Yêu cầu người dùng nhập vào 3 số nguyên dương
    1. Kiểm tra xem đây có phải là số đo 3 cạnh của 1 tam giác không?
    2. Nếu có thì kiểm tra tiếp xem đây là tam giác cân, tam giác đều,
    tam giác vuông hay tam giác thường
    3. Kiểm tra tiếp xem tam giác có góc tù hay không?
    4. Tính diện tích của tam giác
"""
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Check if these 3 numbers are sides of a triangle
if a + b > c and b + c > a and a + c > b:
    if a == b and a == c:
        print("Tam giac deu")
    elif a == b or a == c or b == c:
        if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
            print("Tam giac vuong can")
        else:
            print("Tam giac can")
    elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")
else:
    print("Day khong phai so do 3 canh tam giac")