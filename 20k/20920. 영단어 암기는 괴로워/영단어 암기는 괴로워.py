import sys
input = sys.stdin.readline

C = {}
n, m = map(int, input().split())
for _ in range(n):
    a = str(input().strip())
    if len(a) >= m:   
        if a in C:
            C[a] += 1
        else:
            C[a] = 1

R = sorted(C.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for r in R:
    print(r[0])