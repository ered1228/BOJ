n = int(input()) ; res = 0
A = list(map(float, input().split()))
for a in A:
    res += a**3
print(res**(1/3))