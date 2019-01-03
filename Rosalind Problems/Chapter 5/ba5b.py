n,m = map(int,input().split(" "))
down = list(list())
right = list(list())
for i in range(0,n):
    down.append(list(map(int,input().split(" "))))
dash=input()
for i in range(0,m+1):
    right.append(list(map(int,input().split(" "))))
# print(down)
# print(right)

def findDistance():
    score = list(list())
    for i in range(0,n+1):
        rowScore = list()
        for j in range(0,m+1):
            rowScore.append(0)
        score.append(rowScore)
    for i in range(1,n+1):
        score[i][0] = score[i-1][0] + down[i-1][0]

    for i in range(1,m+1):
        score[0][i] = score[0][i-1] + right[0][i-1]

    for i in range(1,n+1):
        for j in range(1,m+1):
            score[i][j] = max(score[i-1][j]+down[i-1][j],score[i][j-1]+right[i][j-1])
    print(score[n][m])

findDistance()