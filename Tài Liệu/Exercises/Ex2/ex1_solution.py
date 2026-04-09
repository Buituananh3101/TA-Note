"""
    Nhập vào 2 số:
    - 1 số đại diện cho 1 năm
    - 1 số đại diện cho 1 tháng trong năm đó
    In ra màn hình số ngày của tháng đó
    Chú ý: Năm nhuận là năm thỏa mãn 1 trong 2 điều kiện sau:
    - Năm đó chia hết cho 4 nhưng không chia hết cho 100
    - Năm đó chia hết cho 400
"""
year = int(input("Enter year number: "))
month = int(input("Enter month number: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("this month has", 31, "days")
elif month in [4, 6, 9, 11]:
    print("this month has", 30, "days")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("this month has", 29, "days")
    else:
        print("this month has", 28, "days")
else:
    print("Invalid month!")