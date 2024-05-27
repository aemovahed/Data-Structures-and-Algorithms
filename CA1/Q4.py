myStr = input()
for j in range(1, len(myStr), 1):
    num1 = myStr[0:j]
    for k in range(j + 1, len(myStr), 1):
        num2 = myStr[j:k]
        if num2[0] == '0':
            break
        start = k
        while True:
            num3 = int(num1) + int(num2)
            end = start + len(str(num3))
            if end > len(myStr):
                break
            if str(num3) != myStr[start: end]:
                break
            if end == len(myStr):
                print('YES')
                exit()
            num1 = num2
            num2 = num3
            start = end
print('NO')