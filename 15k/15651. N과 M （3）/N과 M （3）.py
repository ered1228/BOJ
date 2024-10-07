from itertools import product

n, m = map(int, input().split())
N = [i for i in range(1, n+1)]
for nums in product(N, repeat=m):
    print(' '.join(map(str, nums)))