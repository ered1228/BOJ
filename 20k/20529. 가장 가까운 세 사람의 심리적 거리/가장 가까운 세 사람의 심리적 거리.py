from itertools import combinations

def sol(a, b, c):
    cnt = 0
    for i in range(4):
        if a[i] != b[i]:
            cnt += 1
        if a[i] != c[i]:
            cnt += 1
        if b[i] != c[i]:
            cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    MBTI = list(input().split())
    dist = float('inf')

    if n > 32:
        print(0)
        continue
    
    P = combinations(MBTI, 3)
    for a, b, c in P:
        dist = min(dist, sol(a, b, c))
    print(dist)