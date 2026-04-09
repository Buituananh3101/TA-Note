"""
    Yêu cầu người dùng nhập vào 2 số bất kỳ.
    Viết chương trình để đổi giá trị 2 số đó với nhau theo 2 cách
"""
a = input("Enter the first value: ")
b = input("Enter the second value: ")
print("Original values: a =", a, ", b =", b)

# First solution: Using a temporary variable
temp = a
a = b
b = temp
print("Swapped values: a =", a, ", b=", b)

# Second solution
a, b = b, a
print("Swapped values: a =", a, ", b=", b)
