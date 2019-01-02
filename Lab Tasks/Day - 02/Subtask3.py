pattern = input()
text = input()
d = int(input())

def findHammingDis(pattern1,pattern2):
    hammingDis = 0
    for i,j in zip(pattern1,pattern2):
        if not i==j:
            hammingDis+=1
    return hammingDis
output = ""
# print(pattern)
for i in range(0,len(text)-len(pattern)+1):
    substr = text[i:i+len(pattern)]
    distance = findHammingDis(pattern,substr)
    # print(distance)
    if distance<=d:
        output+= str(i)+" "
        # print("OK")
print(output)

