from collections import deque

n, k = map(int, input().split())
nlist = list(map(int, input().split()))
A = deque([i for i in range(1, n+1)])
cnt = 0
start = 1

for j in range(k):
    ccw = A.index(nlist[j]) - A.index(start)
    cw = len(A) - A.index(nlist[j])
    if ccw <= cw:
        A.rotate(-ccw)
        A.popleft()
        cnt += ccw
    else:
        A.rotate(cw)
        cnt += cw
        A.popleft()
    if len(A) > 0:
        start = A[0]
print(cnt)