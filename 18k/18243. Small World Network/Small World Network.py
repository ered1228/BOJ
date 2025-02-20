import sys
input = sys.stdin.readline

n, f = map(int, input().split())
M = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
for _ in range(f):
    a, b = map(int, input().split())
    M[a-1][b-1] = 1
    M[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j] = min(M[i][j], M[i][k] + M[k][j])

for r in range(n):
    for c in range(n):
        if M[r][c] > 6:
            print("Big World!")
            exit()
print("Small World!")        