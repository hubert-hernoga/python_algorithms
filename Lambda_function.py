# double x

def double(x):
    return x * 2


print(double(2))


double = lambda x: x * 2


# add x and y


def add(x, y):
    return x + y


print(add(3, 2))


add = lambda x,y: x + y


# max of x, y


def max(x, y):
    if x > y:
        return x
    else:
        return y


print(max(3, 2))


max = lambda x,y: x if x > y else y