from typing import List
from sys import maxsize
INT_MAX = maxsize
INT_MIN = -maxsize
 

time = 1 
def dfs(node, parent, graph, level, t_d, t_f):
    global time
     
    if (parent == -1):
        level[node] = 1
    else:
        level[node] = level[parent] + 1

    t_d[node] = time
    for i in graph[node]:
        if (i != parent):
            time += 1
            dfs(i, node, graph, level, t_d, t_f)
    time += 1
 
    t_f[node] = time


def findLCA(n, graph, v):
    level = [0 for _ in range(n + 1)]
    t_d = [0 for _ in range(n + 1)]
    t_f = [0 for _ in range(n + 1)]
 

    dfs(1, -1, graph, level, t_d, t_f)

    min_t = INT_MAX
    max_t = INT_MIN
    min_v = -1
    max_v = -1
    for i in v:
        if (t_d[i] < min_t):
            min_t = t_d[i]
            min_v = i
        if (t_f[i] > max_t):
            max_t = t_f[i]
            max_v = i
 
    if (min_v == max_v):
        return min_v
 
    lev = min(level[min_v], level[max_v])
    node = 0
    l = INT_MIN
    for i in range(n):
        if (level[i] > lev):
            continue
 
        if (t_d[i] <= min_t and t_f[i] >= max_t and level[i] > l):
            node = i
            l = level[i]
    return node
 

def findParents(parent, start, end):
    p = []
    p.append(start)
    while (start != end):
        p.append(parent[start])
        start = parent[start]
    return p


def printList(li):
    for i in li:
        print(i, end=' ')


def main():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    parent = [None] * (n + 1)
    for _ in range(n - 1):
        p, v = map(int, input().split())
        parent[v] = p
        graph[p].append(v)
        graph[v].append(p)
    k = list(map(int, input().split()))

    r = None
    for i in range(1, n + 1):
        if parent[i] == None:
            r = i
            break
    res = []
    li = findParents(parent, k[0], r)
    res.append(li[::-1])

    for i in range(len(k) - 1):
        lca = findLCA(n, graph, [k[i], k[i + 1]])
        li = findParents(parent, k[i], lca)
        res.append(li[1:])
        li = findParents(parent, k[i + 1], lca)
        res.append(li[-2::-1])

    li = findParents(parent, k[len(k) - 1], r)
    res.append(li[1:-1])

    li = []
    for i in range(len(res)):
        for j in res[i]:
            li.append(j)
    if len(li) == 2 * n - 2:
        printList(li)
    else: print(-1)


if __name__ == "__main__":
    main()