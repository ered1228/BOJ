from collections import deque

def BFS(x, y):
    vis = set()
    queue = deque([(x, y, 0)])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    treasure_dist = 0
    treasure_loc = []
    while queue:
        ti, tj, d = queue.popleft()
        if (ti, tj) not in vis:
            vis.add((ti, tj))
            if d >= treasure_dist:
                treasure_dist = d
                treasure_loc.append((ti, tj))
            for i in range(4):
                ni = ti + di[i]
                nj = tj + dj[i]
                if 0 <= ni < n and 0 <= nj < m and Map[ni][nj] == 'L':
                    queue.append((ni, nj, d+1))
    return treasure_loc, treasure_dist, vis

Map = [] ; land = []
n, m = map(int, input().split())
for i in range(n):
    row = str(input())
    for j in range(m):
        if row[j] == 'L':
            land.append((i, j))
    Map.append(row)

V = set() ; T = []
for l in land:
    if (l[0], l[1]) not in V:
        tresaure_loc, dist, v = BFS(l[0], l[1])
        T.append(tresaure_loc)
        V.update(v)

for t1 in T:
    for t2 in t1:
        x, y = t2[0], t2[1]
        dist = max(dist, BFS(x, y)[1])
print(dist)