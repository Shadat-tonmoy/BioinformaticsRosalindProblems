from itertools import product
from collections import Counter

freq = Counter()
text = input()
chars = "ACGT"
k, d = map(int,input().split(" "))
output = ""
maxCountD = 0

def findHammingDis(pattern1,pattern2):
    hammingDis = 0
    for i,j in zip(pattern1,pattern2):
        if not i==j:
            hammingDis+=1
    return hammingDis

def countD(text,pattern):
    for i in range(0,len(text)-len(pattern)+1):
        subStr = text[i:i+len(pattern)]
        dis = findHammingDis(subStr,pattern)
        if dis<=d:
            freq[pattern]+=1
            global maxCountD
            maxCountD = max(maxCountD,freq[pattern])

# print(k,d)
for i in product(chars,repeat=k):
    kmer = "".join(i)
    # print(kmer)
    countD(text,kmer)

for i in freq:
    if freq[i]==maxCountD:
        output+=i+" "
print(output)

