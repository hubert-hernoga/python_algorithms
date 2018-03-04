# Your goal in this kata is to implement an difference function, which subtracts one list from another.

# It should remove all values from list a, which are present in list b.


def array_diff(a, b):
    for elem in a:
        if elem in b:
            a.remove(elem)
    return list(set(a))


print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2], [1]))
print(array_diff([1, 2, 2], [2]))
print(array_diff([1, 2, 2], []))
print(array_diff([], [1, 2]))