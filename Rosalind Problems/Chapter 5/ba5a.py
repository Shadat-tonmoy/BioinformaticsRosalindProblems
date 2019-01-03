import numpy as np
amount = int(input())
coins = list(map(int,input().split(",")))
def getCoinNum():
    numList = [0]*(amount+1)
    print(numList)
    numList[0] = 0
    for k in range(1, amount+1):
        curMin = np.inf
        for i in coins:
            if k >= i:
                curMin = min(curMin, numList[k-i])
        numList[k] = curMin + 1
    print (numList[-1])

getCoinNum()


# 1,5,10,20,25,50