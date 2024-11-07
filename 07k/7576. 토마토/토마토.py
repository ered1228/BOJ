from collections import deque

def BFS(box, first_tomatos):
    queue = deque([(x, y ,0) for x, y in first_tomatos])
    maxcnt = 0
    
    while queue:
        x, y, cnt = queue.popleft()
        candidate = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for c in candidate:
            tx = c[0] ; ty = c[1]
            if (0 <= tx < n) and (0 <= ty < m):
                if box[tx][ty] == 0:
                    box[tx][ty] = 1
                    queue.append((tx, ty, cnt+1))
                    maxcnt = max(maxcnt, cnt+1)
    return maxcnt, box

m, n = map(int, input().split())
box = [] ; first_tomatos = []

def zero_count(box):
    zero = 0
    for b in box:
        zero += b.count(0)
    if zero == 0:
        return True
    else:
        return False

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            first_tomatos.append((i, j))
    box.append(row)

if not first_tomatos:
    print(-1)
else:
    res, updated_box = BFS(box, first_tomatos)
    if zero_count(updated_box):
        print(res)
    else:
        print(-1)