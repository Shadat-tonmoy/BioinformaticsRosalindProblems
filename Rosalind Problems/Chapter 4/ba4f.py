integerMassTable = {'G': 57,'A': 71,'S': 87,'P': 97,'V': 99,'T': 101,'C': 103,'I': 113,'L': 113,'N': 114,'D': 115,'K': 128,'Q': 128,'E': 129,'M': 131,'H': 137,'F': 147,'R': 156,'Y': 163,'W': 186}
text = input()
spectrum = list(map(int,input().split(" ")))
cyclicText = text*2
unique = set()

unique.add(text)

def findScore():
    output = list()
    for i in range(0,len(text)):
        for j in range(0,len(text)):
            subStr = cyclicText[j:j+i]
            # print(subStr)
            unique.add(subStr)
    for i in unique:
        output.append(getMass(i))
    output.sort()
    score = 0
    # print(output)
    for i in output:
        for j in range(0,len(spectrum)):
            if spectrum[j]==i:
                spectrum[j]=-1
                score+=1
                break
            elif spectrum[j]>i:
                break
    print(score)

def getMass(str):
    mass = 0
    for i in str:
        mass+=integerMassTable[i]
    return mass


findScore()
