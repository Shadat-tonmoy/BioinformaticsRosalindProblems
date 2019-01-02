from collections import Counter
# text = input()
# print(text)
col,row = map(int,input().split(" "))
grid = list(list())

def findConsensus():
    consensusString = ""
    score = 0
    for i in range(0,col):
        freq = Counter()
        maxFreq = 0
        maxFreqChar = ''
        for j in range(0,row):
            # print("At cell (",i," ",j,") value is ",grid[j][i])
            freq[grid[j][i]]+=1
            if freq[grid[j][i]]>maxFreq:
                maxFreq = freq[grid[j][i]]
                maxFreqChar = grid[j][i]
        consensusString+=maxFreqChar+" "
        score+=(row-maxFreq)
    return consensusString,score

for i in range(0,row):
    rowVal = input().split(" ")
    grid.append(rowVal)
consensusString, score = findConsensus()
print("consensusString ",consensusString,"score ",score)



'''
12 10
T C G G G G G T T T T T
C C G G T G A C T T A C
A C G G G G A T T T T C
T T G G G G A C T T T T
A A G G G G A C T T C C
T T G G G G A C T T C C
T C G G G G A T T C A T
T C G G G G A T T C C T
T A G G G G A A C T A C
T C G G G T A T A A C C

'''