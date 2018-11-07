inputPattern = input()
inputString = input()
k =len(inputPattern)
output = ""
for i in range(0,len(inputString)-(k-1)):
    if inputString[i] == inputPattern[0]:
        subStr = inputString[i:i+k]
        if subStr == inputPattern:
            output+=str(i)+" "
print(output)

