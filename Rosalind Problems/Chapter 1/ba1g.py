dna1 = input()
dna2 = input()
hammingDistance = 0
for i in range(0,len(dna1)):
    if dna1[i] != dna2[i]:
        hammingDistance+=1
print(hammingDistance)
