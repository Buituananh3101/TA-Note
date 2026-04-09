"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    tách hàm ban đầu thành 2 nửa, được phân cách bởi
    phần tử có vị trí là k (phần tử này sẽ thuộc về
    nửa thứ 2) rồi sau đó nối chúng lại sao cho nửa
    thứ 2 đứng ở trước nửa thứ nhất
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 3
    Output:
        array = [4, 5, 1, 2, 3]
"""


def split_array(array, k):
    result = array[k:] + array[:k]
    return result

if __name__ == '__main__':
    array = [1, 3, 7, 2, 5, 4]
    print(split_array(array, 3))
