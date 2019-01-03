from itertools import product
from collections import Counter
k = int(input())
dnaString = list()
while True:
    inputStr = input()
    if inputStr:
        # print(inputStr)
        dnaString.append(inputStr)
    else:
        # print("new Line")
        break
chars = "ACGT"
kmers = list()
for i in product(chars,repeat=k):
    kmers.append("".join(i))

def findHammingDistance(pattern1,pattern2):
    dis = 0
    for i,j in zip(pattern1,pattern2):
        if not i==j:
            dis+=1
    return dis

def findMadian():
    madianStr = ""
    minD = 99999999999999
    for kmer in kmers:
        diss = 0
        for dna in dnaString:
            minDis = 9999999999999999
            for i in range(0,len(dna)-len(kmer)+1):
                pattern = dna[i:i+len(kmer)]
                dis = findHammingDistance(pattern,kmer)
                if dis<minDis:
                    minDis = dis
                    # print("Matched ",kmer)
            diss+=minDis
        if diss<=minD:
            minD = diss
            madianStr = kmer
            # print("Matched with ",kmer)
    return madianStr
print(findMadian())


