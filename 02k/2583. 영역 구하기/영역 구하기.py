from collections import deque
import sys
input = sys.stdin.readline

def BFS(stx, sty):
    vis = set()
    queue = deque([(stx, sty)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        if (x, y) not in vis:
            vis.add((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and field[ny][nx] == 0:
                    queue.append((nx, ny))
    return vis, len(vis)

m, n, k = map(int, input().split())
field = [[0]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(m-y2, m-y1):
        for x in range(x1, x2):
            field[y][x] = 1

V = set() ; res = []
for i in range(m):
    for j in range(n):
        if field[i][j] == 0 and (j, i) not in V:
            vis, r = BFS(j, i)
            V.update(vis)
            res.append(r)

res.sort()
print(len(res))
for ele in res:
    print(ele, end=" ")