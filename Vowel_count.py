# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.


def getCount(inputStr):
    vowels = ['a', 'e', 'o', 'u', 'i']
    inputStr = inputStr.lower()
    num_vowels = 0
    for char in inputStr:
        if char in vowels:
            num_vowels += 1
    return num_vowels


def getCount1(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")



print(getCount("abracadabra"))
print(getCount("ewgikuashduiywgt8tj3jg5vmroijiouhaqwsuoydguaQGBIP4YQYIUVBHGFDSAIUKNVBPI9"))
print(getCount("JDSALKIBVYIUABLIREWBKAMNDSKLJBVOAERFBNAHVDJYWEQ"))
print(getCount("safnjkaklsuhbvirhoigfew09t345hg7yviunskiuhuygoui8hgAO8IS7HGF8OIH3QIUH87"))
print('------------------')
print(getCount1("abracadabra"))
print(getCount1("ewgikuashduiywgt8tj3jg5vmroijiouhaqwsuoydguaQGBIP4YQYIUVBHGFDSAIUKNVBPI9"))
print(getCount1("JDSALKIBVYIUABLIREWBKAMNDSKLJBVOAERFBNAHVDJYWEQ"))
print(getCount1("safnjkaklsuhbvirhoigfew09t345hg7yviunskiuhuygoui8hgAO8IS7HGF8OIH3QIUH87"))