# Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

# TODO

def pig_it(text):
    text = text.split(" ")
    count = 0
    for word in text:
        text[count].replace(word[0], word[-1])
        count += 1
    return text


print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))