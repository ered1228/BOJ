import sys
input = sys.stdin.readline

n = int(input())
P = []
for _ in range(n):
    x, y = map(int, input().split())
    P.append((x, y))

D = []
d = 0
for j in range(n-1):
    d += abs(P[j][0]-P[j+1][0]) + abs(P[j][1]-P[j+1][1])

for i in range(1, n-1):
    newd = d + abs(P[i-1][0]-P[i+1][0]) + abs(P[i-1][1]-P[i+1][1])
    newd -= (abs(P[i-1][0]-P[i][0])+abs(P[i-1][1]-P[i][1])+abs(P[i][0]-P[i+1][0]) + abs(P[i][1] - P[i + 1][1]))
    D.append(newd)

print(min(D))