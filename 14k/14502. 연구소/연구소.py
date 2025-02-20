from collections import deque

def virus(I, V):
    T = [i[:] for i in I]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque(V)
    vis = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) not in vis:
            vis.add((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and T[nx][ny] == 0:
                    queue.append((nx, ny))
                    T[nx][ny] = 2
    return sum(row.count(0) for row in T)

n, m = map(int, input().split())
I = [list(map(int, input().split())) for _ in range(n)]
V = []
for r in range(n):
    for c in range(m):
        if I[r][c] == 2:
            V.append((r, c))

res = 0
for i in range(n*m):
    row1 = i // m
    col1 = i % m
    for j in range(i+1, n*m):
        row2 = j // m
        col2 = j % m
        for k in range(j+1, n*m):
            row3 = k // m
            col3 = k % m
            if I[row1][col1] + I[row2][col2] + I[row3][col3] == 0:
                I[row1][col1] = 1
                I[row2][col2] = 1
                I[row3][col3] = 1
                res = max(res, virus(I, V))
                I[row1][col1] = 0
                I[row2][col2] = 0
                I[row3][col3] = 0

print(res)