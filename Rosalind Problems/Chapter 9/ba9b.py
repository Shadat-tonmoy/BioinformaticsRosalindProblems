text = input()
output = []
lenght = len(text)
while (1):
    inputString = input()
    if len(inputString) == 0:
        break
    pos = 0

    while (pos < lenght):
        pos = text.find(inputString, pos)
        if pos == -1:
            break
        else:
            output.append(pos)
            pos = pos + 1

output.sort()
print(" ".join(output))
