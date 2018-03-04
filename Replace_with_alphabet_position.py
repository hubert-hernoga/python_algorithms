"""
Required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

a being 1, b being 2, etc.
"""
import string


def alphabet_position(text):
    text = text.lower()
    zip_list = list(zip(list(string.ascii_lowercase), list(range(1,27))))
    dict = {}
    array = []
    for element in zip_list:
        dict[element[0]] = element[1]
    for letter in text:
        if letter in dict:
            array.append(dict[letter])
    return " ".join(str(x) for x in array)


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position1(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')


def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
print('-----------------')
print(alphabet_position1("The sunset sets at twelve o' clock."))
print(alphabet_position1("The narwhal bacons at midnight."))
print('-----------------')
print(alphabet_position2("The sunset sets at twelve o' clock."))
print(alphabet_position2("The narwhal bacons at midnight."))
