from functools import reduce
from operator import mul


def persistence(number, count=0):
    # recursion base case - exit once the number is less than 10
    if number < 10:
        return count

    # get new number by multiplying digits of a number
    new_number = reduce(mul, map(int, str(number)))

    return persistence(new_number, count + 1)


print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))