from collections import deque
import sys
input = sys.stdin.readline

def BFS(stx, sty):
    jururu = set()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    gosegu = 0
    lilpa = deque([(stx, sty)])
    
    while lilpa:
        x, y = lilpa.popleft()
        if (x, y) not in jururu:
            jururu.add((x, y))
            ine[x][y] = 2
            gosegu += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and ine[nx][ny] == 1:
                    lilpa.append((nx, ny))
    return gosegu               

n, m = map(int, input().split())
ine = [] ; viichan = []
for _ in range(n):
    jingburger = list(map(int, input().split()))
    ine.append(jingburger)

for i in range(n):
    for j in range(m):
        if ine[i][j] == 1:
            viichan.append(BFS(i, j))

if viichan:
    print(len(viichan))
    print(max(viichan))
else:
    print(0)
    print(0)