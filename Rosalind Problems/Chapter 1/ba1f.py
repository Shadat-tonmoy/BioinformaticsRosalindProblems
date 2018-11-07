inputString = input()
countC = 0
countG = 0
minSkew = 999999999999999999999999
skewList = list()
output = ""
for i in range(0,len(inputString)):
    diff = countG - countC
    skewList.append(diff)
    minSkew = min(minSkew,diff)
    if inputString[i] == 'C':
        countC+=1
    elif inputString[i] == 'G':
        countG+=1
for i in range(0,len(skewList)):
    if skewList[i] == minSkew:
        output+= str(i)+" "
print(output)
