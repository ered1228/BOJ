from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [] ; cheese = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            cheese.append((i, j))
    table.append(row)

#2-marking
outqueue = deque([(0, 0)])
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
while outqueue:
    oi, oj = outqueue.popleft()
    if table[oi][oj] == 0:
        table[oi][oj] = 2
        for k in range(4):
            ni, nj = oi + di[k], oj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and table[ni][nj] == 0:
                outqueue.append((ni, nj))

t = 0
while cheese:
    next_cheese = [] ; melt_cheese = []
    for chi, chj in cheese:
        melt = 0
        for k in range(4):
            ci, cj = chi + di[k], chj + dj[k]
            if table[ci][cj] == 2:
                melt += 1
        if melt < 2:
            next_cheese.append((chi, chj))
        else:
            table[chi][chj] = 0
            melt_cheese.append((chi, chj))
    
    #2-marking update
    queue = deque(melt_cheese)
    while queue:
        mci, mcj = queue.popleft()
        if table[mci][mcj] == 0:
            table[mci][mcj] = 2
            for k in range(4):
                nmci, nmcj = mci + di[k], mcj + dj[k]
                if 0 <= nmci < n and 0 <= nmcj < m and table[nmci][nmcj] == 0:
                    queue.append((nmci, nmcj))

    #time
    cheese = next_cheese
    t += 1

print(t)