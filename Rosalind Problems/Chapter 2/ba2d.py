profileRow = {'A': 0, 'C':1, 'G':2, 'T':3}
def makeProfile(kMers):

    k = len(kMers[0])
    t = len(kMers)
    profile = list(dict())
    for i in range(0,k):
        profileCol = {'A':0, 'C':0, 'G':0, 'T':0}
        for j in range(0,t):
            profileCol[kMers[j][i]] += 1
        for key in profileCol.keys():
            profileCol[key] = 1.0 * profileCol[key] / t
        profile.append(profileCol)
    return profile

def getPatternProbability(profile, pattern):
    probability = 1
    for i in range(0, len(pattern)):
        probability *= profile[i][pattern[i]]
    return probability

def getProfileMostProbableKmer(dna, profile, k):
    startIndex = 0
    length = len(dna)
    maxProbability = 0
    mostProbable = dna[0:k]
    while startIndex + k <= length:
        subStr = dna[startIndex:startIndex+k]
        probability = getPatternProbability(profile, subStr)
        if probability > maxProbability:
            mostProbable = subStr
            maxProbability = probability
        startIndex += 1
    return mostProbable

def getHammingDistance(a, b):
    diff = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff

def makeConsensus(motifes):
    profile = makeProfile(motifes)
    consensusList = list()
    for item in profile:
        consensusList.append(max(item, key=item.get))
    return ''.join(consensusList)

def getScore(motifes):
    consensus = makeConsensus(motifes)
    score = 0
    for motif in motifes:
        score += getHammingDistance(consensus, motif)

    return score

def greedyMotifSearch(Dna, k, t):
    bestMotif = list()
    for i in range(0,t):
        bestMotif.append(Dna[i][0:k])
    start = 0
    length = len(Dna[0])
    while start + k <= length:
        motifes = list()
        motifes.append(Dna[0][start:start+k])
        for i in range(1, t):
            profile = makeProfile(motifes[0:i])
            motifes.append(getProfileMostProbableKmer(Dna[i], profile, k))
        if getScore(motifes) < getScore(bestMotif):
            bestMotif = motifes[:]
        start += 1
    for element in bestMotif:
        print (element)

    return bestMotif


DNA = "GGCGTTCAGGCA AAGAATCAGTCA CAAGGAGTTCGC CACGTCAATCAC CAATAATATTCG".split(" ")
greedyMotifSearch(DNA, 3, 5)
