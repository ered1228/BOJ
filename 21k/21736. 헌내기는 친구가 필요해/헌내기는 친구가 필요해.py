from collections import deque
import sys
input = sys.stdin.readline

def BFS(st):
    queue = deque([(st[0], st[1])])
    cnt = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        loc = campus[x][y]
        if loc != 'V' and loc != 'X':
            if loc == 'P':
                cnt += 1
            campus[x][y] = 'V'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if campus[nx][ny] == 'O' or campus[nx][ny] == 'P':
                        queue.append((nx, ny))
    return cnt

campus = []
st = None
n, m = map(int, input().split())
for i in range(n):
    inp = [_ for _ in str(input().rstrip())]
    for j in range(m):
        if inp[j] == 'I':
            st = (i, j)
    campus.append(inp)

res = BFS(st)
if res == 0:
    print('TT')
else:
    print(res)