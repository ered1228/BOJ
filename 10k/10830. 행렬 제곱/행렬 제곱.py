def cross(A, B):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
                res[i][j] %= 1000
    return res

n, e = map(int, input().split())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

I = [[0]*n for _ in range(n)]
for inx in range(n):
    I[inx][inx] = 1

while e != 0:
    if e % 2 == 1:
        I = cross(mat, I)
    mat = cross(mat, mat)
    e //= 2

for r in I:
    print(" ".join(map(str, r)))