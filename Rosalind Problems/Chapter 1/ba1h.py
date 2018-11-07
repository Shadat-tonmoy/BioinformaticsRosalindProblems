inputPattern = input()
inputString = input()
d = int(input())
k = len(inputPattern)
def findHammingDistance(a,b):
    distance = 0
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            distance+=1
    return distance
output = ""
for i in range(0,len(inputString)-(k-1)):
    subStr = inputString[i:i+k]
    if findHammingDistance(inputPattern,subStr) <= d:
        output+=str(i)+" "
print(output)