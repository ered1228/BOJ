import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a-1][b-1] = min(c, adj[a-1][b-1])

for i in range(n):
    for j in range(n):
        if i == j:
            adj[i][j] = 0
        elif adj[i][j] == 0:
            adj[i][j] = float('inf')

for k in range(n):
    for i in range(n):
        for j in range(n):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for r in range(n):
    for c in range(n):
        if adj[r][c] == float('inf'):
            print(0, end=" ")
        else:
            print(adj[r][c], end=" ")
    print()