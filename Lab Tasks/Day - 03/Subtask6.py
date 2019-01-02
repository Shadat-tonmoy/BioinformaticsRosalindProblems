pattern = input()
dnaString = list(input().split(" "))

def findHammingDistance(pattern1,pattern2):
    dis = 0
    for i,j in zip(pattern1,pattern2):
        if not i==j:
            dis+=1
    return dis



def findDistanceBetweenPatternAndStrings(pattern):
    k = len(pattern)
    distance = 0
    for dna in dnaString:
        hammingDistance = 9999999999
        for i in range(0,len(dna)-k+1):
            kmer = dna[i:i+k]
            _hammingDistance = findHammingDistance(pattern,kmer)
            if hammingDistance > _hammingDistance:
                hammingDistance = _hammingDistance
        distance += hammingDistance
    return distance

print(findDistanceBetweenPatternAndStrings(pattern))

'''
AAA
TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT
'''