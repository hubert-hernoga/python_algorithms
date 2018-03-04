"""
def find_missing(sequence):
    count = 0
    diff = sequence[1] - sequence[0]
    sequence1 = []
    quant = len(sequence1) - len(sequence)
    while len(sequence1) != (len(sequence)):
        if len(sequence1) == 0:
            sequence1.append(sequence[0])
        if len(sequence1) != 0:
            sequence1.append(sequence[count] + int(diff))
            count += 1
    missing_num = sum(sequence1) - sum(sequence)
    print(sequence)
    print(sequence1)
    return missing_num
"""
'''
def find_missing(sequence):
    if sequence[0] < sequence[1]:
        diff = sequence[1] - sequence[0]
        diff1 = sequence[2] - sequence[1]
        diff2 = []
        diff2.append(diff)
        diff2.append(diff1)
        diff2 = sorted(diff2)
        sequence1 = list(range(sequence[0], sequence[-1] + diff2[0]))
        sequence1 = sequence1[::diff2[0]]
        for num in sequence1:
            if num not in sequence:
                sequence.insert(0, num)
        return sequence[0]
    else:
        diff = sequence[0] - sequence[1]
        diff1 = sequence[1] - sequence[2]
        diff2 = []
        diff2.append(diff)
        diff2.append(diff1)
        diff2 = sorted(diff2)
        sequence1 = list(range(sequence[-1], sequence[0] + diff2[0]))
        sequence1 = sequence1[::diff2[0]]
        for num in sequence1:
            if num not in sequence:
                sequence.insert(0, num)
        return sequence[0]
'''


def find_missing(sequence):
    l_r = []
    for i in range(1, len(sequence)):
        r = sequence[i] - sequence[i - 1]
        l_r.append(r)
    l_ratio = [abs(r) for r in l_r]
    r_max = max(l_ratio)
    i_max = l_ratio.index(r_max)
    ratio = l_r[i_max] / 2

    return int(sequence[i_max] + ratio)


def find_missing1(sequence):
    return (sequence[-1] + sequence[0]) * (len(sequence) + 1) / 2 - sum(sequence)


print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
print(find_missing([1, 3, 7, 9]))
print(find_missing([2, 6, 8, 10]))
print(find_missing([1, 6, 11, 16, 21, 31]))
print(find_missing([2, 4, 8, 10, 12, 14]))
print(find_missing([1,11,31,41,51]))
print(find_missing([25, 21, 17, 13, 5, 1]))
print('-----------')
print(find_missing1([1, 2, 3, 4, 6, 7, 8, 9]))
print(find_missing1([1, 3, 7, 9]))
print(find_missing1([2, 6, 8, 10]))
print(find_missing1([1, 6, 11, 16, 21, 31]))
print(find_missing1([2, 4, 8, 10, 12, 14]))
print(find_missing1([1,11,31,41,51]))
print(find_missing1([25, 21, 17, 13, 5, 1]))
