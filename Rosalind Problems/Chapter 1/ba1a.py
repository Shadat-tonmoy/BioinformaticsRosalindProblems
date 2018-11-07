inputString = input()
inputPattern = input()
countFreq = 0

for i in range(0,len(inputString)):
    if inputString[i]==inputPattern[0]:
        a = inputString[i:i+len(inputPattern)]
        if a == inputPattern:
            countFreq+=1
print(countFreq)
