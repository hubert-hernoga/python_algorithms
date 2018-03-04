#Make a program that filters a list of strings and returns a list with only your friends name in it.

#If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...



def friend(x):
    array = []
    for names in x:
        if len(names) == 4:
            array.append(names)
    return array


def friend1(x):
    return [names for names in x if len(names) == 4]


print(friend(["Ryan", "Kieran", "Mark"]))
print(friend(['Ryan', '123', '4']))
print('-----------------------------')
print(friend1(["Ryan", "Kieran", "Mark"]))
print(friend1(['Ryan', '123', '4']))