inputString = input()

length = len(inputString)

last = []

for i in range(0, length):
    last.append(inputString[i])

First = sorted(last)
# print(last,First)
a = []

a = First
for i in range(0, length - 1):
    temp = []
    for j in range(0, length):
        temp.append("" + last[j] + a[j])

    # print(temp)
    temp.sort()

    a = temp

s = a[0]
s = s[1:len(s)] + s[0]

print(s)