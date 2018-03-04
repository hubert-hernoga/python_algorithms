def DNA_strand1(dna):
    word = ""
    for i in dna:
        if i == 'A':
            i = 'T'
            word += i
        elif i == 'T':
            i = 'A'
            word += i
        elif i == 'C':
            i = 'G'
            word += i
        elif i == 'G':
            i = 'C'
            word += i
    return word


def DNA_strand2(dna):  # Drugi sposób
    return dna.translate(str.maketrans("ATCG", "TAGC"))


pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def DNA_strand3(dna):
    return ''.join([pairs[x] for x in dna])


print(DNA_strand1('AATGC'))
print(DNA_strand1('ATACC'))
print("---------------------")
print(DNA_strand2('AATGC'))
print(DNA_strand2('ATACC'))
print("---------------------")
print(DNA_strand3('AATGC'))
print(DNA_strand3('ATACC'))
