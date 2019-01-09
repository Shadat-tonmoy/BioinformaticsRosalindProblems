inputStr = input()

ara = []

str1 = input()

length = len(str1)

z = ""
for i in range(0, length):
    if str1[i] == ' ':
        ara.append(z)
        z = ""
        continue
    if str1[i] >= 'A' and str1[i] <= 'Z':
        z = z + str1[i]
    if i == length - 1:
        ara.append(z)
        continue

# print(ara)
l1 = len(ara)
length = len(inputStr)
ans = []
for n in range(0, l1):
    pattern = ara[n]

    pos = 0
    while (pos < length):
        pos = inputStr.find(pattern, pos)
        if pos > -1:
            ans.append(pos)
            pos = pos + 1
        else:
            break
ans.sort()
for i in ans:
    print(i, end=" ")