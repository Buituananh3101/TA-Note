"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Trả về kết quả là 1 list, trong đó các phần tử bị dịch
    sang trái k đơn vị
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 2
    Output:
        array = [3, 4, 5, 1, 2]
"""


def shift_array(array, k):
    num_elements = len(array)

    new_array = [0] * num_elements  # new array to store the shifted elements

    for i in range(num_elements):
        new_array[i] = array[(i + k) % num_elements]

    return new_array


if __name__ == '__main__':
    array = [1, 3, 7, 2, 5, 4]
    print(shift_array(array, 13))
