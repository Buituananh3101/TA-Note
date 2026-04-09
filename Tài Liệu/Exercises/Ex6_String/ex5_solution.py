"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    đếm và trả về số lượng nguyên âm trong chuỗi đó
"""


def count_vowels(string):
    vowels = "aeiou"
    count = 0
    string = string.lower()
    for vowel in vowels:
        count += string.count(vowel)
    return count


text = "Today is a beautiful day"
print(count_vowels(text))
