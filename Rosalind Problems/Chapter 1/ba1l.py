inputString = input()
numberMap = {'A':0, 'C':1, 'G':2, 'T':3}
def getNumberForPattern(pattern):
    if not pattern:
        return 0
    return 4 * getNumberForPattern(pattern[:-1]) + numberMap[pattern[-1]]
print (getNumberForPattern(inputString))