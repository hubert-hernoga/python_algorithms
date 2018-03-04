"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items
without any elements with the same value next to each other and preserving the original order of elements.
"""
from itertools import groupby


def unique_in_order(iterable):
    arr = list(iterable)
    arr1 = []
    while len(arr) != 1:
        if len(arr) == 0:
            return arr
        elif arr[1] == arr[0]:
            del arr[0]
        else:
            arr1.append(arr[0])
            del arr[0]
    arr1.append(arr[0])
    return arr1


def unique_in_order1(iterable):
    a = list(iterable)
    n = len(a)
    i = 0
    b = []
    while i < n:
        j = i + 1
        while j < n and a[i] == a[j]:
            j += 1
        b.append(a[i])
        i = j
    return b

def unique_in_order2(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


def unique_in_order3(iterable):
    return [k for (k, _) in groupby(iterable)]


print(unique_in_order([]))
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print('---------------------')
print(unique_in_order1([]))
print(unique_in_order1('AAAABBBCCDAABBB'))
print(unique_in_order1('ABBCcAD'))
print(unique_in_order1([1, 2, 2, 3, 3]))
print('---------------------')
print(unique_in_order2([]))
print(unique_in_order2('AAAABBBCCDAABBB'))
print(unique_in_order2('ABBCcAD'))
print(unique_in_order2([1, 2, 2, 3, 3]))
print('---------------------')
print(unique_in_order3([]))
print(unique_in_order3('AAAABBBCCDAABBB'))
print(unique_in_order3('ABBCcAD'))
print(unique_in_order3([1, 2, 2, 3, 3]))