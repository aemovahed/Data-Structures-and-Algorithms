N = int(input())
num = input().split()
pos = [0] * (N + 1)
for i in range(N):
    num[i] = int(num[i])
    pos[num[i]] = i + 1
prev = [0] * (N + 1)
stack = []
for i in range(N, 0, -1):
    while (True):  
        if len(stack) == 0:
            stack.append(pos[i])
            break
        elif stack[-1] < pos[i]:
            prev[pos[i]] = stack[-1]
            stack.append(pos[i])
            break
        elif stack[-1] > pos[i]:
            stack.pop()
stack = []
ans = 0
for i in range(1, N + 1, 1):
    print(ans)
    flag = False
    if len(stack):
        if pos[i] < stack[-1]:
            stack.pop()
            ans = ans - 1
    if prev[pos[i]] != 0 and len(stack) == 0:
        ans = ans + 1
        stack.append(pos[i])
        flag = True
    if len(stack) == 0 or flag == True:
        continue
    if prev[pos[i]] != 0 and prev[pos[i]] != prev[stack[-1]]:
        ans = ans + 1
        stack.append(pos[i])       
print(ans)