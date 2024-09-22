from itertools import permutations

n, m = map(int, input().split())
P = [i for i in range(1, n+1)]
A = list(permutations(P, m))

for a in A:
    print(" ".join(map(str, a)))