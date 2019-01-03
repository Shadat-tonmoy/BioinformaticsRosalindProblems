k = int(input())
text = input()
output = list()
for i in range(0,len(text)-k+1):
    kmer = text[i:i+k]
    output.append(kmer)
output.sort()
for i in output:
    print(i)
