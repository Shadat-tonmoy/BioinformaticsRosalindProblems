from collections import Counter
inputString = input()
k =int(input())
freqCounter = Counter()
maxFreq = 0
for i in range(0,len(inputString)-(k-1)):
    subStr = inputString[i:i+k]
    freqCounter[subStr]+=1
    maxFreq = max(maxFreq,freqCounter[subStr])

for i in freqCounter:
    if freqCounter[i]==maxFreq:
        print(i)


