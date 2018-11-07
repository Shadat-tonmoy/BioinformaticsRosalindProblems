inputString = input()
reverseMap = {'A':'T','T':'A','C':'G','G':'C'}
reverseString = inputString[::-1]
complimentedString = ""
for i in range(0,len(inputString)):
    complimentedString+=reverseMap[reverseString[i]]
print(complimentedString)