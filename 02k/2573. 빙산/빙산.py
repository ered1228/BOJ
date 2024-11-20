from collections import deque
import sys
input = sys.stdin.readline

def count_segment(initial):
    V = set() ; c = 0
    for x, y in initial:
        if iceberg[x][y] != 0 and (x, y) not in V:
            V.update(BFS(x, y))
            c += 1
    return c

def BFS(stx, sty):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    vis = set()
    queue = deque([(stx, sty)])
    while queue:
        x, y = queue.popleft()
        if (x, y) not in vis:
            vis.add((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] > 0:
                    queue.append((nx, ny))
    return vis

def melting(iceberg):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    new_iceberg = [row[:] for row in iceberg]
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                temp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] == 0:
                        temp += 1
                new_iceberg[i][j] = max(0, iceberg[i][j]-temp)
    return new_iceberg

def all_zero(M):
    for i in range(n):
        for j in range(m):
            if M[i][j] != 0:
                return False
    return True

n, m = map(int, input().split())
iceberg = [] ; initial = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] != 0:
            initial.append((i, j))
    iceberg.append(row)

cnt = 0 ; res = 0
while True:
    if all_zero(iceberg):
        res = 0
        break
    else:
        seg = count_segment(initial)
        if seg > 1:
            res = cnt
            break
        else:
            iceberg = melting(iceberg)
            cnt += 1
print(res)