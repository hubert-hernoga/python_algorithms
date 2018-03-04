def code(c):
    c = list(c)
    count = 6
    if c[2] == "-":
        while count != 0:
            for char in c:
                if char in "1234567890-":
                    count -= 1
                else:
                    return "wrong number"
        a = "".join(c)
        return a
    else:
        return "wrong number"



print(code("13-345"))