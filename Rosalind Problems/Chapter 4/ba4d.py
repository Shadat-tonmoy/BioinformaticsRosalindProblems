peptideMasses = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def calcVarinats(m):
    ways = [0]*(m + 1)
    index = m
    ways[m] = 1
    while index > 0:
        for key in peptideMasses:
            ways[index-key] += ways[index]

        index -= 1
        while ways[index] == 0:
            index -= 1
    print(ways[0])

n = int(input())
calcVarinats(n)






