import sys
from collections import deque
input = sys.stdin.readline

def BFS(sx, sy):
    vis = set()
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()
        if (x, y) not in vis:
            vis.add((x, y))
            S = [(x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1),
                 (x, y-1), (x-1, y+1), (x-1, y), (x-1, y-1)]
            for s in S:
                if 0 <= s[0] < h and 0 <= s[1] < w and M[s[0]][s[1]] == 1:
                    queue.append(s)
    return vis

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    M = []
    for _ in range(h):
        row = list(map(int, input().split()))
        M.append(row)
    res = 0 ; V = set()
    for i in range(h):
        for j in range(w):
            if M[i][j] == 1 and (i, j) not in V:
                res += 1
                V.update(BFS(i, j))
    print(res)