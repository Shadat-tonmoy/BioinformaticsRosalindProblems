text = input()
k = int(input())
profile = dict()
chars = "ACGT"

def checkProbability(kmer):
    probability = 1
    for i in range(0,len(kmer)):
        char = kmer[i]
        prob = profile[char][i]
        probability*=prob
        # print("Probabilit of ",char," At pos ",i," is ",prob)
    return probability

def findProfileMostKMer():
    maxProb = 0
    profileMostKmer = ''
    for i in range(0,len(text)-k+1):
        kmer = text[i:i+k]
        print(kmer)
        prob = checkProbability(kmer)
        if prob>maxProb:
            maxProb = prob
            profileMostKmer = kmer
    return profileMostKmer,maxProb


for i in chars:
    profile[i] = list(map(float,input().split(" ")))
# print(profile)
profileMostKMer, maxProb = findProfileMostKMer()
print("profileMostKMer ",profileMostKMer, " maxProb ",maxProb)

'''
ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2
'''
