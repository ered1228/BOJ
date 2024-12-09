from collections import deque

def BFS(B, start, color):
    queue = deque([start])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    while queue:
        temp = queue.popleft()
        if B[temp[0]][temp[1]] == color:
            B[temp[0]][temp[1]] = 'C'
            cnt += 1
            for i in range(4):
                nx = temp[0] + dx[i]
                ny = temp[1] + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    queue.append((nx, ny))
    return cnt

n, m = map(int, input().split())
B = []
for _ in range(m):
    war = [w for w in str(input())]
    B.append(war)

c1, c2 = 0, 0
for i in range(m):
    for j in range(n):
        if B[i][j] == 'W':
            c1 += (BFS(B, (i, j), 'W'))**2
        elif B[i][j] == 'B':
            c2 += (BFS(B, (i, j), 'B'))**2

print(c1, c2)