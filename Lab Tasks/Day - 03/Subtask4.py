from collections import Counter
row,col = map(int,input().split(" "))
grid = list(list())

def getProfile():
    output = dict()
    output['A'] = list()
    output['C'] = list()
    output['G'] = list()
    output['T'] = list()
    for i in range(0,col):
        freq = Counter()
        for j in range(0,row):
            freq[grid[j][i]]+=1
        output['A'].append(str(freq['A'])+"/"+str(row))
        output['C'].append(str(freq['C'])+"/"+str(row))
        output['G'].append(str(freq['G'])+"/"+str(row))
        output['T'].append(str(freq['T'])+"/"+str(row))
    return output





for i in range(0,row):
    rowVal = list(input())
    grid.append(rowVal)
output = getProfile()
print('A : ',output['A'])
print('C : ',output['C'])
print('G : ',output['G'])
print('T : ',output['T'])


'''

5 6
TCGGGG
CCGGTG
ACGGGG
TTGGGG
AATACG

'''