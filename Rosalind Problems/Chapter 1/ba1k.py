import itertools
inputString = input()
k = int(input())
allPosCom = set(itertools.combinations(inputString,k))
allPosComList = list()
for i in allPosCom:
    allPosComList.append("".join(i))
allPosComList = sorted(allPosComList)
ans = list()
for i in allPosComList:
    count = 0
    for j in range(0,len(inputString)-(k-1)):
        subStr = inputString[j:j+k]
        if subStr == i:
            count+=1
    ans.append(str(count))
print(" ".join(ans))




