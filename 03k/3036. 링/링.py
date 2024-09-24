import math

n = int(input())
ring = list(map(int, input().split()))
for j in range(1, n):
    d = math.gcd(ring[0], ring[j])
    print(f"{ring[0] // d}/{ring[j] // d}")