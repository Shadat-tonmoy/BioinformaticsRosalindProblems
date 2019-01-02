from itertools import product
text = input()
k,l,t = map(int,input().split(" "))
chars = "ACGT"


def doesFormClump(pattern):
    for i in range(0,len(text)-l+1):
        subText = text[i:i+l]
        freq = subText.count(pattern)
        if freq>=t:
            return True
    return False



for i in product(chars,repeat=k):
    kmer = "".join(i)
    if doesFormClump(kmer):
        print(kmer)
