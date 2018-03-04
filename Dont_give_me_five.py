# In this kata you get the start number and the end number of a region and should return the count
# of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!


def dont_give_me_five(start, end):
    numbers = []
    for i in range(start, end + 1):
        i = str(i)
        numbers.append(i)
        if i[0] == "5" or i[-1] == "5":
            numbers.remove(i)
        else:
            for char in i:
                if char == "5":
                    numbers.remove(i)
                    print(numbers)
    return len(numbers)


def dont_give_me_five1(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))


print(dont_give_me_five(1, 9))
print(dont_give_me_five(4, 17))
print(dont_give_me_five(0, 100))
print("-----------------")
print(dont_give_me_five1(1, 9))
print(dont_give_me_five1(4, 17))
print(dont_give_me_five1(0, 100))