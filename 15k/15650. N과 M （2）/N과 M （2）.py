from itertools import combinations

n, m = map(int, input().split())
C = [i for i in range(1, n+1)]
for nums in combinations(C, m):
    print(' '.join(map(str, nums)))