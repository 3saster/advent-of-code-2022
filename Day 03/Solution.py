def commonElement(comps):
    common = comps[0]
    for c in comps:
        common = list(set(common).intersection(c))
    return common

def priority(char):
    if ord('a') <= ord(char) <= ord('z'):
        return ord(char)-ord('a')+1
    elif ord('A') <= ord(char) <= ord('Z'):
        return ord(char)-ord('A')+27 


def Part1(data):
    common = []
    for rucksack in data:
        compLen = len(rucksack)//2
        common += commonElement([rucksack[:compLen],rucksack[compLen:]])
    return sum(priority(c) for c in common)

def Part2(data):
    common = []
    for rucksacks in [[data[3*i],data[3*i+1],data[3*i+2]] for i in range(len(data)//3)]:
        common += commonElement(rucksacks)
    return sum(priority(c) for c in common)