text = input()
spectrum = list(map(int,input().split(" ")))
integerMassTable = {'G': 57,'A': 71,'S': 87,'P': 97,'V': 99,'T': 101,'C': 103,'I': 113,'L': 113,'N': 114,'D': 115,'K': 128,'Q': 128,'E': 129,'M': 131,'H': 137,'F': 147,'R': 156,'Y': 163,'W': 186}

def getMass(string):
    mass = 0
    for i in string:
        mass+=integerMassTable[i]
    return mass

def getLinearScore():
    output = list()
    output.append(0)
    for i in range(0,len(text)):
        for j in range(0,len(text)):
            if i+j <= len(text):
                kmer = text[j:i+j]
                output.append(getMass(kmer))
    output.append(getMass(text))
    score = 0
    for i in range(0,len(output)):
        for j in range(0,len(spectrum)):
            if output[i] == spectrum[j]:
                spectrum[j]=-1
                score+=1
                break
            elif spectrum[j]>output[i]:
                break
    print(score)

getLinearScore()



