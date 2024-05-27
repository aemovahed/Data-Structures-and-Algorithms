empty_teams = [False] * 2


def dfs(adj, mark, noted_teams, std):
    mark[std] = True
    used_teams = [False] * 2

    for e in adj[std]:
        if noted_teams[e] == 0:
            used_teams[0] = True
        elif noted_teams[e] == 1:
            used_teams[1] = True

    if used_teams[0] == False and used_teams[1] == False:
        if not empty_teams[0]: noted_teams[std] = 0
        elif not empty_teams[1]: noted_teams[std] = 1
        else: noted_teams[std] = 0
    elif used_teams[0] == False and used_teams[1] == True:
        noted_teams[std] = 0
    elif used_teams[0] == True and used_teams[1] == False:
        noted_teams[std] = 1
    else:
        noted_teams[std] = 0


    for e in adj[std]:
        if not mark[e]:
            dfs(adj, mark, noted_teams, e)


def makeEnmityGraph(n, m):
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    return adj


def main():
    n, m = map(int, input().split())
    adj = makeEnmityGraph(n, m)

    noted_teams = [-1] * (n + 1)
    mark = [False] * (n + 1)

    for s in range(1, n + 1, 1):
        if not mark[s]:
            dfs(adj, mark, noted_teams, s)

    count = 0
    res = []
    for s in range(1, len(noted_teams), 1):
        if noted_teams[s] == 0: 
            count += 1
            res.append(s)

    print(count)
    for std in res:
        print(std, end=' ')

            
if __name__ == "__main__":
    main()