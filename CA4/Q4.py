from sys import maxsize as INT_MAX 
from collections import deque 

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Node: 
    def __init__(self, to, weight, coord): 
        self.to = to 
        self.weight = weight
        self.coord = coord


def zeroOneBFS(k, edges, src): 
    dist = [[INT_MAX, None] for _ in range(k)]
   
    Q = deque() 
    dist[src][0] = 0
    Q.append(src) 
  
    while Q: 
        v = Q[0] 
        Q.popleft() 
  
        for i in range(len(edges[v])): 
            if (dist[edges[v][i].to][0] > dist[v][0] + edges[v][i].weight): 
                dist[edges[v][i].to][0] = dist[v][0] + edges[v][i].weight
                dist[edges[v][i].to][1] = edges[v][i].coord
                if edges[v][i].weight == 0: 
                    Q.appendleft(edges[v][i].to) 
                else: 
                    Q.append(edges[v][i].to) 
  
    return dist

def addEdge(edges, u, v, u_coord, v_coord, wt):
    edges[u].append(Node(v, wt, v_coord)) 
    edges[v].append(Node(u, wt, u_coord)) 


def main():
    n, m, k = map(int, input().split())
    coords = []
    for _ in range(k):
        y, x = map(int, input().split())
        coords.append(Coord(x, y))
    
    edges = [[] for _ in range(k)]
    for i in range(k):
        for j in range(i + 1, k):
            if abs(coords[i].x - coords[j].x) == 1 and abs(coords[i].y - coords[j].y) == 1:
                addEdge(edges, i, j, coords[i], coords[j], 0)
            elif abs(coords[i].x - coords[j].x) <= 2 or abs(coords[i].y - coords[j].y) <= 2:
                addEdge(edges, i, j, coords[i], coords[j], 1)
    
    src = 0
    dist = zeroOneBFS(k, edges, src)
    li = []
    for d in dist:
        if d[1] == None: continue
        if d[1].x == m and d[1].y == n:
            print(d[0])
            return
        elif m - d[1].x <= 1 or n - d[1].y <= 1:
            li.append(d[0] + 1)
    print(min(li))



if __name__ == "__main__":
    main()