integerMassTable = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                    'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
text = input()

def getMass(str):
    weight = 0
    for x in str:
        weight += integerMassTable[x]
    return weight


def buildCyclicSequence():
    output = [0]
    for i in range(1, len(text)):
        for j in range(len(text)):
            if i + j > len(text):
                k = i + j - len(text)
                output.append(getMass(text[j:] + text[:k]))
            else:
                output.append(getMass(text[j:i + j]))
    output.append(getMass(text))
    output.sort()
    print(" ".join(str(e) for e in output))


buildCyclicSequence()