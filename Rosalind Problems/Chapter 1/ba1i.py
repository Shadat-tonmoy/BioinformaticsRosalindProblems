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

for i in range(0,len(inputString)-(k-1)):
    subStr = inputString[i:i+k]
    kMerList.append(subStr)
maxFreq = 0
for i in kMerList:
    for j in range(0, len(inputString) - (k - 1)):
        subStr = inputString[j:j + k]
        if findHammingDistance(i,subStr) <= d:
            freqCounter[subStr]+=1
            maxFreq = max(maxFreq,freqCounter[subStr])

for i in freqCounter:
    if freqCounter[i] == maxFreq:
        print(i)




