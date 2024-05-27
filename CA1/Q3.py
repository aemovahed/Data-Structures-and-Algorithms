myList = []
maxLen = 1
str = input()
for i in range(len(str)):
    for j in range(i, len(str), 1):
        if str[j] in myList:
            break
        myList.append(str[j])
    if maxLen < len(myList):
        maxLen = len(myList)
    myList.clear()
print(maxLen)