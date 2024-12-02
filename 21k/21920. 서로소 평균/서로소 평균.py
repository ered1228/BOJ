import math

n = int(input())
A = list(map(int, input().split()))
X = int(input())
B = []
for a in A:
    if math.gcd(a, X) == 1:
        B.append(a)
print(sum(B)/len(B))