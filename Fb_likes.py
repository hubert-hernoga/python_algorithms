# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.


def likes(names):
    if len(names) == 1:
        return "%s likes this" % (names[0])
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    elif len(names) > 3:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names) - 2)
    else:
        return 'no one likes this'


print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Iva', 'Angi']))