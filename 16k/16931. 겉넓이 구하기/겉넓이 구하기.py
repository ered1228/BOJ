n, m = map(int, input().split())
A = [[0 for col in range(m+2)] for row in range(n+2)]
B = [[0]*(m+2)]
res = 0

for _ in range(n):
    C = list(map(int, input().split()))
    C.insert(0, 0)
    C.append(0)
    B.append(C)

B.append([0]*(m+2))

for i in range(1, n+1):
    for j in range(1, m+1):
        if B[i][j] > B[i+1][j]:
            A[i][j] += B[i][j] - B[i+1][j]
        if B[i][j] > B[i-1][j]:
            A[i][j] += B[i][j] - B[i-1][j]
        if B[i][j] > B[i][j+1]:
            A[i][j] += B[i][j] - B[i][j+1]
        if B[i][j] > B[i][j-1]:
            A[i][j] += B[i][j] - B[i][j-1]
for a in A:
    res += sum(a)
print(res + (2*n*m))