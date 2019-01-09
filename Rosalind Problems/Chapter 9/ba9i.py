inputStr = input()

lenght = len(inputStr)

inputStr = inputStr + inputStr

output = []

for i in range(0, lenght):
    output.append(inputStr[i:i + lenght])
output.sort()

la = len(output)
ans = ""
for i in range(0,la):
    ans = ans + output[i][lenght - 1]
print(ans)