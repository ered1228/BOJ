import sys
input = sys.stdin.readline

I = []
n, m = map(int, input().split())
for i in range(n):
    R = list(map(int, input().split()))
    for j in range(m):
        if R[j] == 1:
            I.append((i+1, j+1))
print(abs(I[0][0] - I[1][0]) + abs(I[0][1] - I[1][1]))