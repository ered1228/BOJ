from itertools import combinations
import math

A = list(map(int, input().split()))
C = combinations(A, 3)
R = []
for c in C:
    R.append(math.lcm(c[0], c[1], c[2]))

print(min(R))