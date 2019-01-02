inputString = input()
revMap = {'A':'T','G':'C','C':'G','T':'A'}
outputString = ""
for i in inputString:
    outputString+=revMap[i]
outputString = outputString[::-1]
print(outputString)