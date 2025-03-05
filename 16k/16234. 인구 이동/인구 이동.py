from collections import deque
import sys
input = sys.stdin.readline

def popdiff(i1, j1, i2, j2):
    if l <= abs(nations[i1][j1] - nations[i2][j2]) <= r:
        return True
    return False

def union(cx, cy):
    U = set([(cx, cy)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([(cx, cy)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in U and popdiff(x, y, nx, ny):
                queue.append((nx, ny))
                U.add((nx, ny))
    return U

n, l, r = map(int, input().split())
nations = []
for _ in range(n):
    nations.append(list(map(int, input().split())))

cnt = 0
while True:
    unions = []
    unions_check = set()
    for i in range(n):
        for j in range(n):
            if (i, j) in unions_check:
                continue
            V = union(i, j)
            if len(V) != 1:
                unions.append(V)
                unions_check.update(V)
    
    if not unions:
        break
    
    for U in unions:
        s = sum(nations[u[0]][u[1]] for u in U)
        s //= len(U)
        for u in U:
            nations[u[0]][u[1]] = s  
    cnt += 1

print(cnt)