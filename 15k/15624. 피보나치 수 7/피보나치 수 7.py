F = [0, 1, 1, 2]
n = int(input())
for i in range(4, 1000001):
    F.append((F[i-1] + F[i-2])%1000000007)
print(F[n])