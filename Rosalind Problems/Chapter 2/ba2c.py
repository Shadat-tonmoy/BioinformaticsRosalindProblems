profile_row = {'A': 0, 'C':1, 'G':2, 'T':3}
def readProfileMatrix(fileName):
    with open(fileName) as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    data = list(list())
    for i in range(0, len(lines)):
        data.append(lines[i].split())

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            data[i][j] = float(data[i][j])

    return data

def getPatternProbability(profile, pattern):
    probability = 1
    for i in range(0, len(pattern)):
        probability *= profile[profile_row[pattern[i]]][i]

    return probability

def getProfileMostProbableKmer(dna, profile, k):
    startIndex = 0
    length = len(dna)
    maxProbability = 0
    mostProbable = ''
    while startIndex + k <= length:
        subStr = dna[startIndex:startIndex+k]
        probability = getPatternProbability(profile, subStr)
        if probability > maxProbability:
            mostProbable = subStr
            maxProbability = probability

        startIndex += 1

    print (mostProbable)

if __name__ == "__main__":
    data = readProfileMatrix("in.txt")
    getProfileMostProbableKmer("TGACCTGGATAACAG", data, 6)
