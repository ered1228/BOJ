import heapq
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
M = []
for _ in range(n):
    row = [int(r) for r in str(input().rstrip())]
    M.append(row)

break_cnt = [[float('inf')]*m for i in range(n)]
break_cnt[0][0] = 0
queue = []
heapq.heappush(queue, (0, 0, 0))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    cnt, x, y = heapq.heappop(queue)
    if break_cnt[x][y] < cnt:
        continue
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < n and 0 <= ny < m:
            if M[nx][ny] == 0:
                w = 0
            else:
                w = 1
            if break_cnt[nx][ny] > cnt + w:
                break_cnt[nx][ny] = cnt + w
                heapq.heappush(queue, (cnt+w, nx, ny))

print(break_cnt[n-1][m-1])