A = [] ; B = []

n, m = map(int, input().split())
for _ in range(n):
    a1 = list(map(int, input().split()))
    A.append(a1)
m, k = map(int, input().split())
for _ in range(m):
    b1 = list(map(int, input().split()))
    B.append(b1)

res = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            res[i][j] += A[i][l]*B[l][j]
for r in res:
    print(" ".join(map(str, r)))