N = int(input())
canvas = []
for _ in range(N):
    canvas.append(int(input()))
li = []
start = 0
end = -1
for i in range(N):
    if canvas[i] == 0:
        if i == 0:
            start = 1
        elif i != 0 and canvas[i - 1] == 0:
            start += 1
        else:
            end = i
    if i == N - 1 and end == -1:
        end = N
    if start > N - 1:
        start = -1
    if start != -1 and end != -1:
        li.append(canvas[start:end])
        start = end + 1
        end = -1
if len(li) == 0:
    print(-1)
    exit()
result = [[0]] * len(li)
r = [0] * len(li)
numOfColor = [0] * (N + 1)
visit = [False] * (N + 1)
group = [-1] * (N + 1)
numOfTimes = [[0]] * (N + 1)
for i in range(len(li)):
    stack = []
    for color in li[i]:
        numOfColor[color] += 1
    for color in li[i]:
        if visit[color] == True:
            numOfColor[color] -= 1
            if group[color] != i:
                print(-1)
                exit()
            while stack[-1] != color:
                if numOfColor[stack[-1]] > 1:
                    print(-1)
                    exit()
                temp = stack.pop()
                numOfColor[temp] -= 1
                val = max(numOfTimes[temp])
                if val == 0:
                    val += 1
                numOfTimes[temp] = [0]
                if numOfTimes[color] == [0]:
                    numOfTimes[color] = [val]
                else:
                    numOfTimes[color].append(val)
            stack.pop()
            numOfColor[color] -= 1
            val = max(numOfTimes[color]) + 1
            numOfTimes[color] = [0]
            if len(stack) == 0:
                if result[i] == [0]:
                    result[i] = [val]
                else:
                    result[i].append(val)
            else:
                if numOfTimes[stack[-1]] == [0]:
                    numOfTimes[stack[-1]] = [val]
                else: 
                    numOfTimes[stack[-1]].append(val)     
            if numOfColor[color] > 0:
                stack.append(color)
                numOfColor[color] += 1
        else:
            stack.append(color)
            visit[color] = True
            group[color] = i
    l = max(numOfTimes)
    a = max(l)
    b = max(result[i])
    if a > b:
        r[i] = a
    else:
        r[i] = b
    if a == 0 and b == 0 and len(stack) != 0:
        r[i] = 1
print(max(r))