"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""


def move_zeros(array):
    for element in array:
        if type(element) == int and element < 1:
            del array[array.index(element)]
            array.append(0)
        elif type(element) == bool:
            array[array.index(element)] = format(False)
            pass
    return array


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]))
print(move_zeros([0, 1, None, 2, False, 1, 0]))
print(move_zeros(["a", "b"]))
print(move_zeros(["a"]))
print(move_zeros([0, 0]))
print(move_zeros([0]))
print(move_zeros([]))