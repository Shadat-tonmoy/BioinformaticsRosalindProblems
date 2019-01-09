inputStr = input()

length = len(inputStr)

last = []

for i in range(0, length):
    last.append(inputStr[i])

First = sorted(last)
# print(last,First)
ara = []

ara = First
for i in range(0, length - 1):
    temp = []
    for j in range(0, length):
        # print(last[j],ara[j])
        temp.append("" + last[j] + ara[j])

    # print(temp)
    temp.sort()

    ara = temp
    # print("->",ara)
inputStr = ara[0]
inputStr = inputStr[1:len(inputStr)] + inputStr[0]

# print(st)

ara = []
st1 = input()

length = len(st1)

z = ""
for i in range(0, length):
    if st1[i] == ' ':
        ara.append(z)
        z = ""
        continue
    if st1[i] >= 'A' and st1[i] <= 'Z':
        z = z + st1[i]
    if i == length - 1:
        ara.append(z)
        continue
l1 = len(ara)
length = len(inputStr)
for i in range(0, l1):
    pattern = ara[i]
    pos = 0
    count = 0
    while (pos < length):
        pos = inputStr.find(pattern, pos)
        if pos == -1:
            break
        else:
            pos = pos + 1
            count = count + 1
    print(count, end=" ")