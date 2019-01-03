integerMassTable = {'G': 57,'A': 71,'S': 87,'P': 97,'V': 99,'T': 101,'C': 103,'I': 113,'L': 113,'N': 114,'D': 115,'K': 128,'Q': 128,'E': 129,'M': 131,'H': 137,'F': 147,'R': 156,'Y': 163,'W': 186}
aminoAcidTable = ['G','A','S','P','V','T','C','I','L','N','D','K','Q','E','M','H','F','R','Y','W']
text = input()
cyclicText = text*2
unique = set()

unique.add(text)

def buildLinearSpectrum():
    output = list()
    output.append(0)
    for i in range(1,len(text)):
        for j in range(len(text)):
            if i+j <= len(text):
                kmer = text[j:j+i]
                output.append(getMass(kmer))
    output.append(getMass(text))

    output.sort()
    print(" ".join(str(e) for e in output))


def getMass(str):
    mass = 0
    for i in str:
        mass+=integerMassTable[i]
    return mass
buildLinearSpectrum()