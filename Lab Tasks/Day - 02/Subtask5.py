from collections import Counter
from itertools import product
text = input()
k,d = map(int,input().split(" "))
freq = Counter()
maxCountD = 0
chars = "ACGT"
output = ""

def findHammingDistance(pattern1,pattern2):
    hammingDis = 0
    for i,j in zip(pattern1,pattern2):
        if not i==j:
            hammingDis+=1
    return hammingDis

def findReverseCompliment(pattern):
    reverseMap = {'A':'T','T':'A','C':'G','G':'C'}
    revComp = ""
    for i in pattern:
        revComp+=reverseMap[i]
    revComp=revComp[::-1]
    return revComp

def findRevCountD(text,pattern):
    for i in range(0,len(text)-len(pattern)+1):
        global maxCountD
        subStr = text[i:i+len(pattern)]
        _pattern = findReverseCompliment(pattern)
        dis = findHammingDistance(subStr,pattern)
        _dis = findHammingDistance(subStr,_pattern)
        if dis <=d:
            freq[pattern]+=1
            maxCountD = max(maxCountD,freq[pattern])
        if _dis <=d:
            freq[pattern]+=1
            maxCountD = max(maxCountD,freq[pattern])

for i in product(chars,repeat=k):
    kmer = "".join(i)
    findRevCountD(text,kmer)

# print(freq)
for i in freq:
    if freq[i]==maxCountD:
        output+=i+" "
print(output)



