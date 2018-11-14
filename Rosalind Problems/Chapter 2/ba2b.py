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

def getMinDistanceInString(dna, pattern):
    dnaList = list()
    startIndex = 0
    lengthOfDNA = len(dna)
    k = len(pattern)
    while startIndex + k <= lengthOfDNA:
        substr = dna[startIndex:startIndex+k]
        dnaList.append(getHammingDistance(substr, pattern))
        startIndex += 1
    return min(dnaList)

def getDistanceInDNASet(Dna, pattern):
    distances = list()
    for dna in Dna:
        distances.append(getMinDistanceInString(dna, pattern))
    return sum(distances)

def getMedianStr(Dna, k):
    allCombination = getAllPossibleCom(k)
    answers = dict()
    for kMer in allCombination:
        answers[kMer] = getDistanceInDNASet(Dna, kMer)

    print (min(answers, key=answers.get))

k = 3
DNA = "AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTACGGGACAG".split(" ")
getMedianStr(DNA, k)