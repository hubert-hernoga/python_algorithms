"""
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position t
he word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive
numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
"""


def order(sentence):
    words = sentence.split()
    result = []
    for n in range(1,10):
        for word in words:
            if str(n) in word:
                result.append(word)
    return ' '.join(result)


def order1(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


print(order("is2 Thi1s T4est 3a"))
print('----------------')
print(order1("is2 Thi1s T4est 3a"))