from collections import deque

def BFS(stx, sty):
    vis = set()
    queue = deque([(stx, sty)])
    
    while queue:
        i, j = queue.popleft()
        if M[i][j] == 1 and (i, j) not in vis:
            vis.add((i, j))
            S = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for s in S:
                if 0 <= s[0] < n and 0 <= s[1] < n and M[s[0]][s[1]] == 1:
                    if s not in vis:
                        queue.append((s[0], s[1]))
    return len(vis), vis

M = [] ; res = [] ; V = set()
n = int(input())
for _ in range(n):
    row = str(input())
    inrow = []
    for r in row:
        inrow.append(int(r))
    M.append(inrow)

startset = [(i, j) for i in range(n) for j in range(n)]
for stx, sty in startset:
    if ((stx, sty) not in V) and (M[stx][sty] == 1):
        size, v = BFS(stx, sty)
        res.append(size)
        V.update(v)

res.sort()
print(len(res))
for ine in res:
    print(ine)