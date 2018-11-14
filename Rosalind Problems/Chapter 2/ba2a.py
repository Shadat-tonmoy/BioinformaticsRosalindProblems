import itertools

def getAllPossibleCom(k):
    combinations = map(''.join, itertools.product('ACTG', repeat=k))
    answers = dict()
    for combination in combinations:
        answers[combination] = 0
    return sorted(answers)

def getHammingDistance(a, b):
    diff = 0
    for i in range(0,len(a)):
        if a[i] != b[i]:
            diff+= 1
    return diff

def motifEnumeration(data, k, d):
    Patterns = set(getAllPossibleCom(k))
    PatternsCopy = Patterns.copy()
    for dna in data:
       currentSet = set()
       start = 0
       length = len(dna)
       while start + k <= length:
           substr = dna[start: start + k]
           for item in PatternsCopy:
               if getHammingDistance(substr, item) <= d:
                   currentSet.add(item)
           start += 1
       Patterns = Patterns & currentSet
    for item in Patterns:
        print (item)

k,d = 3,1
data = "ATTTGGC TGCCTTA CGGTATC GAAAATT".split(" ")
motifEnumeration(data, 5, 1)