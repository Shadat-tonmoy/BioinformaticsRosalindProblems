inputStr = list()
overlapGraph = list()
while True:
    str = input()
    if str:
        inputStr.append(str)
    else :
        break

def buildOverlapGraph():
    for str in inputStr:
        prefix = str[0:len(str)-1]
        suffix = str[1:]
        for i in inputStr:
            if not i==str and suffix in i:
                overlapGraph.append(str+" -> "+i)
                break
    overlapGraph.sort()
buildOverlapGraph()

for i in overlapGraph:
    print(i)

