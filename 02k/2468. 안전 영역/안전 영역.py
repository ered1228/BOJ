from collections import deque

def BFS(A, stx, sty):
    nA = [row[:] for row in A]
    vis = set()
    queue = deque([(stx, sty)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        if (x, y) not in vis:
            vis.add((x, y))
            nA[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and A[nx][ny] == 1:
                    queue.append((nx, ny))
    return nA

def new_area(Area, height):
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = Area[i][j] - height
            if temp > 0:
                A[i][j] = 1
            else:
                A[i][j] = 0
    return A

n = int(input())
Area = []
minh, maxh = float('inf'), 1
for _ in range(n):
    row = list(map(int, input().split()))
    for r in row:
        maxh = max(maxh, r)
        minh = min(minh, r)
    Area.append(row)

res = [1]
for h in range(minh, maxh):
    cnt = 0
    nA = new_area(Area, h)
    for i in range(n):
        for j in range(n):
            if nA[i][j] == 1:
                nA = BFS(nA, i, j)
                cnt += 1
    res.append(cnt)
print(max(res))