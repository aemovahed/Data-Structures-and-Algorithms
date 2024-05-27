n = int(input())
t = int(input())
scenario = [input() for _ in range(t)]

for s in scenario:
    s, t = s.split()
    count = [0] * 2
    k = 0
    while k < 2:
        if k == 0:
            start = s
            target = t
        else:
            start = s[::-1]
            target = t[::-1]
        for i in range(n):
            for j in range(i, n):
                if target[i] == start[j]:
                    if i == j: break
                    start = list(start)
                    tmp = start[j::-1]
                    tmp = tmp[:len(tmp) - i]
                    start[i:j + 1] = tmp
                    start = ''.join(start)
                    count[k] += 1
                    break
            if start == target: break
        k += 1
    print(min(count))