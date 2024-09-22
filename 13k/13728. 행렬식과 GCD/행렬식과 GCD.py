import math

n = int(input())
F = [0, 1, 1] #2, 3, 5
for i in range(3, n+2):
    F.append(F[i-1] + F[i-2])

res = 0
for j in range(1, n+1):
    inx = math.gcd(n+1, j+1)
    res += F[inx]

print(res % ((10**9) + 7))