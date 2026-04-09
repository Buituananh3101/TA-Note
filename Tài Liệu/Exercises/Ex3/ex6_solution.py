"""
    Yêu cầu người dùng nhập vào 1 số dạng nhị phân (e.g. 1001)
    In ra giá trị dạng thập phân tương ứng của số đó
"""
n = input("Enter a binary number: ")
# First solution
print(int(n, 2))

# Second solution
num_digits = len(n)
result = 0
position = 0  # Position of each digit (increase from left to right)
for digit in n:
    result += int(digit)*2**(num_digits-position-1)
    position += 1
print(result)


