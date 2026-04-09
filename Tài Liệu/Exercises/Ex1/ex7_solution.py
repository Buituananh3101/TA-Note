"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên bất kì
    Lấy ra chữ số hàng đơn vị theo 2 cách khác nhau
    rồi in ra màn hình
"""
# First solution
n = int(input("Enter a number: "))
print("The unit digit is", n % 10)

# Second solution
s = input("Enter a number: ")
print("The unit digit is", s[-1])
