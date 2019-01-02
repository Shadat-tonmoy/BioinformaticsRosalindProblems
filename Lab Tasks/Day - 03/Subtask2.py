text = input()
numG = 0
numC = 0
minDiff = 99999999999999999
for i in text:
    if i=='G':
        numG+=1
    elif i=='C':
        numC+=1
    diff = numG-numC
    minDiff = min(minDiff,diff)

numC = 0
numG = 0
output = ""
for i in range(0,len(text)):
    if text[i]=='G':
        numG+=1
    elif text[i]=='C':
        numC+=1
    diff = numG-numC
    if diff==minDiff:
        output+=str(i+1)+" "
print(output)




