inputStr = list()
while True:
    string = input()
    if string:
        inputStr.append(string)
    else :
        break
output = inputStr[0]
for i in range(1,len(inputStr)):
    output+=inputStr[i][len(inputStr[i])-1]
print(output)