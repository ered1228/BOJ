from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Map = [list(map(int, input().strip())) for _ in range(n)]
dist = [[[-1]*2 for _ in range(m)] for _ in range(n)]

queue = deque([(0, 0, 0)])
dist[0][0][0] = 1
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
while queue:
    r, c, cost = queue.popleft()
    if r == n-1 and c == m-1:
        print(dist[r][c][cost])
        break

    for i in range(4):
        nr = r + di[i]
        nc = c + dj[i]
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        if Map[nr][nc] == 1 and dist[nr][nc][1] == -1 and cost == 0:
            dist[nr][nc][1] = dist[r][c][0] + 1
            queue.append((nr, nc, 1))
        elif Map[nr][nc] == 0 and dist[nr][nc][cost] == -1:
            dist[nr][nc][cost] = dist[r][c][cost] + 1
            queue.append((nr, nc, cost))
else:
    print(-1)