"""
    Tìm số lớn nhất và nhỏ nhất trong dãy sau
"""
numbers = [2, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3]

# # First solution: Use built-in functions
# print("Max value is", max(numbers))
# print("Min value is", min(numbers))

# Second solution:
from math import inf

min_value = inf
max_value = -inf
for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
print("Max value is", max_value)
print("Min value is", min_value)
