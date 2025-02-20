from itertools import combinations

n = int(input())
S = list(map(int, input().split()))
mv = [True] + [False]*2000000

for i in range(1, n+1):
    P = combinations(S, i)
    for p in P:
        mv[sum(p)] = True

for idx, val in enumerate(mv):
    if not val:
        print(idx)
        exit()