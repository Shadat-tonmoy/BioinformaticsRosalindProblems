str1 = input()
str2 = input()
hammingDis = 0
for i,j in zip(str1,str2):
    if not i==j:
        hammingDis+=1
print(hammingDis)
