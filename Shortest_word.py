def shortest_word(string):
    split = string.split(" ")
    shortest = split[0]
    for words in split:
        if len(words) < len(shortest):
            shortest = words
    return len(shortest)


def shortest_word1(s):
    return min(len(x) for x in s.split())


print(shortest_word("Basic Tests"))
print(shortest_word("bitcoin take over the world maybe who knows perhaps"))
print(shortest_word("turns out random test cases are easier than writing out basic ones"))
print(shortest_word("lets talk about javascript the best language"))
print(shortest_word("i want to travel the world writing code one day"))
print(shortest_word("Lets all go on holiday somewhere very cold"))
print('----------------')
print(shortest_word1("Basic Tests"))
print(shortest_word1("bitcoin take over the world maybe who knows perhaps"))
print(shortest_word1("turns out random test cases are easier than writing out basic ones"))
print(shortest_word1("lets talk about javascript the best language"))
print(shortest_word1("i want to travel the world writing code one day"))
print(shortest_word1("Lets all go on holiday somewhere very cold"))