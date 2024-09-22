n, k = map(int, input().split())
factor = []

for i in range(1, n+1):
    if n % i == 0:
        factor.append(i)

if len(factor) < k:
    print(0)
else:
    print(factor[k-1])