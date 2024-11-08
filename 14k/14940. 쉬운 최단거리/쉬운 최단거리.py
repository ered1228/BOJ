from collections import deque

def BFS(stx, sty):
    vis = set()
    R = [[0]*m for _ in range(n)]
    queue = deque([(stx, sty, 0)])
    
    while queue:
        x, y, cnt = queue.popleft()
        R[x][y] = cnt
        if (x, y) not in vis:
            vis.add((x, y))
            S = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for s in S:
                if 0 <= s[0] < n and 0 <= s[1] < m and M[s[0]][s[1]] == 1:
                    if s not in vis:
                        queue.append((s[0], s[1], cnt+1))
    return R

n, m = map(int, input().split())
M = []
for i in range(n):
    row = list(map(int, input().split()))
    for idx, r in enumerate(row):
        if r == 2:
            stx, sty = i, idx
    M.append(row)

R = BFS(stx, sty)

for e1 in range(n):
    for e2 in range(m):
        if M[e1][e2] == 1 and R[e1][e2] == 0:
            R[e1][e2] = -1

for row in R:
    print(" ".join(map(str, row)))