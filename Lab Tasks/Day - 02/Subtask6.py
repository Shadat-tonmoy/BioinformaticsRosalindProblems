pattern = input();

def symbolToNumber(symbol):
    if symbol == "A":
        number = 0
    elif symbol == "C":
        number = 1
    elif symbol == "G":
        number = 2
    elif symbol == "T":
        number = 3
    return number

def patternToNumber(Pattern):
    patternList = list(Pattern)
    if not patternList:
        return 0
    symbol = patternList[-1]
    prefix = patternList[:-1]
    print("Symbol ",symbol," Prefix ",prefix)
    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)

print(patternToNumber(pattern))

