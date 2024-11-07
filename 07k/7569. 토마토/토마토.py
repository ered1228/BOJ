from collections import deque

def BFS(box, first_tomatos):
    queue = deque([(x, y, z, 0) for x, y, z in first_tomatos])
    maxcnt = 0
    
    while queue:
        x, y, z, cnt = queue.popleft()
        candidate = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]
        for c in candidate:
            tx = c[0] ; ty = c[1] ; tz = c[2]
            if (0 <= tx < h) and (0 <= ty < n) and (0 <= tz < m):
                if box[tx][ty][tz] == 0:
                    box[tx][ty][tz] = 1
                    queue.append((tx, ty, tz, cnt+1))
                    maxcnt = max(maxcnt, cnt+1)
    return maxcnt, box

def zero_count(box):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return False
    return True

m, n, h = map(int, input().split())
box = [] ; first_tomatos = []

for k in range(h):
    layer = []
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if row[j] == 1:
                first_tomatos.append((k, i, j))
        layer.append(row)
    box.append(layer)

if not first_tomatos:
    print(-1)
else:
    res, updated_box = BFS(box, first_tomatos)
    if zero_count(updated_box):
        print(res)
    else:
        print(-1)