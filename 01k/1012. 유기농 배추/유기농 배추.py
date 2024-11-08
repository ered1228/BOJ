from collections import deque
import sys
input = sys.stdin.readline

def BFS(stx, sty):
    vis = set()
    queue = deque([(stx, sty)])
    while queue:
        x, y = queue.popleft()
        if (x, y) not in vis:
            vis.add((x, y))
            S = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for s in S:
                if 0 <= s[0] < m and 0 <= s[1] < n and field[s[1]][s[0]] == 1:
                    queue.append(s)
    return vis

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    startset = set() ; V = set() ; cnt = 0
    
    for _ in range(k):
        X, Y = map(int, input().split())
        field[Y][X] = 1
        startset.add((X, Y))
    
    for stx, sty in startset:
        if (stx, sty) not in V:
            v = BFS(stx, sty)
            cnt += 1
            V.update(v)
    print(cnt)