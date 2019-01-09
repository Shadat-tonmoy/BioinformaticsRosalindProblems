def buildTrie(patterns):
    myDict = {}
    myDict['A'] = 0
    myDict['C'] = 1
    myDict['G'] = 2
    myDict['T'] = 3

    trie = [[-1 for j in range(4)]]
    last = 0

    for pattern in patterns:
        current = 0
        for ch in pattern:

            if trie[current][myDict[ch]] != -1:
                current = trie[current][myDict[ch]]
            else:
                last += 1
                print(str(current) + '->' + str(last) + ':' + ch)
                temp = [-1 for j in range(4)]
                trie.append(temp)
                trie[current][myDict[ch]] = last
                current = last


str_input = input()

patterns = []
for i in str_input.split():
    patterns.append(i)

buildTrie(patterns)