from collections import deque

def candidate(x, y, z):
    return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]

def BFS(box, first_tomatos):
    queue = deque([(a, b, c, 0) for a, b, c in first_tomatos])
    maxcnt = 0
    
    while queue:
        z, x, y, cnt = queue.popleft()
        for tz, tx, ty in candidate(z, x, y):
            if 0 <= tz < h and 0 <= tx < n and 0 <= ty < m:
                if box[tz][tx][ty] == 0:
                    box[tz][tx][ty] = 1
                    queue.append((tz, tx, ty, cnt+1))
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
box = []
first_tomatos = []

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