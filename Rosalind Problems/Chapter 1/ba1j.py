from collections import Counter
inputString = input()
k,d = map(int,input().split(" "))
kMerList = list()
visited = dict()

def findHammingDistance(a,b):
    distance = 0
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            distance+=1
    return distance

output = ""
freqCounter = Counter()


def getReverseComplement(str):
    reverseMap = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverseString = str[::-1]
    complimentedString = ""
    for i in range(0, len(str)):
        complimentedString += reverseMap[reverseString[i]]
    return complimentedString


for i in range(0,len(inputString)-(k-1)):
    subStr = inputString[i:i+k]
    kMerList.append(subStr)

# for i in kMerList:
#     print(i)

maxFreq = 0
for i in kMerList:
    if freqCounter[i]==0:
        for j in range(0, len(inputString) - (k - 1)):
            subStr = inputString[j:j + k]
            if findHammingDistance(i,subStr) <= d:
                freqCounter[i]+=1
                # print("OK for ",subStr)
                # maxFreq = max(maxFreq,freqCounter[i])
            if findHammingDistance(getReverseComplement(i),subStr) <=d:
                freqCounter[getReverseComplement(i)]+=1
                # print("OK for ",subStr)
                # maxFreq = max(maxFreq,freqCounter[i])
            maxFreq = max(maxFreq, freqCounter[i]+freqCounter[getReverseComplement(i)])

for i in freqCounter:
    print(i,"--> ",freqCounter[i])
    if freqCounter[i] == maxFreq:
        output+=i+" "
print(output)




