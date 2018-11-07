from collections import Counter
inputString = input()
k,l,t = map(int,input().split(" "))
visited = dict()
output = ""
for i in range(0,len(inputString)-(l-1)):
    subStrOfL = inputString[i:i+l]
    freqCounter = Counter()
    for j in range(0,len(subStrOfL)-(k-1)):
        kMer = subStrOfL[j:j+k]
        freqCounter[kMer]+=1
        if freqCounter[kMer] == t:
            if not kMer in visited:
                output+=kMer+" "
                visited[kMer] = True
print(output)
