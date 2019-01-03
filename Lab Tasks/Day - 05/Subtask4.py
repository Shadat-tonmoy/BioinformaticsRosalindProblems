k = int(input())
inputStr = input()
deBrujnGraph = dict()
keys = list()
for i in range(0,len(inputStr)-k+1):
    a = inputStr[i:i+k-1]
    b = inputStr[i+1:i+k]
    if not a in deBrujnGraph:
        deBrujnGraph[a] = list()
        keys.append(a)
    deBrujnGraph[a].append(b)
keys.sort()
for key in keys:
    deBrujnGraph[key].sort()
    print(key+" -> "+",".join(deBrujnGraph[key]))
