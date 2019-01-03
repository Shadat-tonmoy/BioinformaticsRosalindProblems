inputStr = list()
deBrujinGraph = dict()
keys = list()

while True:
    str = input()
    if str:
        inputStr.append(str)
    else:
        break
for str in inputStr:
    a = str[0:len(str)-1]
    b = str[1:len(str)]
    if not a in deBrujinGraph:
        deBrujinGraph[a] = list()
        keys.append(a)
    deBrujinGraph[a].append(b)
keys.sort()
for key in keys:
    deBrujinGraph[key].sort()
    print(key+" -> "+",".join(deBrujinGraph[key]))