import sys
input = sys.stdin.readline

def find(a):
    if a != capital[a]:
        capital[a] = find(capital[a])
    return capital[a]

n, m = map(int, input().split())
A = [0]
capital = [i for i in range(n+1)]
rank = [0]*(n+1)
for _ in range(n):
    A.append(int(input()))
for _ in range(m):
    o, p, q = map(int, input().split())
    p, q = find(p), find(q)
    if o == 1:
        if rank[p] < rank[q]:
            capital[p] = q
            A[q] += A[p]
            A[p] = 0
        elif rank[p] > rank[q]:
            capital[q] = p
            A[p] += A[q]
            A[q] = 0
        else:
            capital[p] = q
            A[q] += A[p]
            A[p] = 0
            rank[q] += 1
    else:
        if A[p] < A[q]:
            A[q] -= A[p]
            capital[p] = q
            if rank[p] == rank[q]:
                rank[q] += 1
            A[p] = 0
        elif A[p] > A[q]:
            A[p] -= A[q]
            capital[q] = p
            if rank[p] == rank[q]:
                rank[p] += 1
            A[q] = 0
        else:
            rank[p] = 0
            rank[q] = 0
            A[p] = 0
            A[q] = 0
            capital[p] = q

cnt = 0 ; res = []
for a in A:
    if a > 0:
        cnt += 1
        res.append(a)
res.sort()
print(cnt)
print(*res)