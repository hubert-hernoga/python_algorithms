"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    str_square = ""
    for digit in str(num):
        str_square += str(int(digit) ** 2)
    return int(str_square)


print(square_digits(9119))
