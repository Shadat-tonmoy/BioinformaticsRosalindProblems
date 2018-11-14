numberMap = {0:'A', 1:'C', 2:'G', 3:'T'}
index = int(input())
k = int(input())
def getPattern(index, k):
    if k == 1:
        return numberMap[index]
    prefixIndex = index / 4
    r = index % 4
    prefixPattern = getPattern(prefixIndex, k - 1)
    return prefixPattern + numberMap[r]
print (getPattern(index, k))