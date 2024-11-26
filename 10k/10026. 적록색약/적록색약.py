from collections import deque
import sys
input = sys.stdin.readline

def BFS(stx, sty, M):
    vis = set()
    queue = deque([(stx, sty)])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    while queue:
        ci, cj = queue.popleft()
        if (ci, cj) not in vis:
            vis.add((ci, cj))
            color = M[ci][cj]
            M[ci][cj] = 'V'
            for i in range(4):
                ni = ci + di[i]
                nj = cj + dj[i]
                if 0 <= ni < n and 0 <= nj < n:
                    if M[ni][nj] == color:
                        queue.append((ni, nj))

n = int(input())
A = [] ; B = []
for _ in range(n):
    row = str(input())
    A.append([r for r in row])
    B.append([r for r in row.replace('G', 'R')])

cnt1, cnt2 = 0, 0
V1 = set() ; V2 = set()
for i in range(n):
    for j in range(n):
        if A[i][j] != 'V':
            cnt1 += 1
            BFS(i, j, A)
        if B[i][j] != 'V':
            cnt2 += 1
            BFS(i, j, B)

print(cnt1, cnt2)