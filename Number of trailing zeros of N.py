"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

http://mathworld.wolfram.com/Factorial.html

N! = 1 * 2 * 3 * 4 ... N


"""
from math import factorial


def zeros(n):
    result = str(factorial(n))
    result = result[::-1]
    count = 0
    for char in result:
        count += 1
        if char != "0":
            break
    print(result)
    return count - 1



print(zeros(6))
print("-------")
zeros(15)
print("-------")
zeros(22)
print("-------")
zeros(4)
print("-------")
zeros(77)
print("-------")
zeros(199)
print("----100---")
