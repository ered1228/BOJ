import math

def gcdf(N):
    l = len(N)
    G = []
    for i in range(l):
        for j in range(i+1, l):
            G.append(math.gcd(N[i], N[j]))
    return max(G)

t = int(input())
for _ in range(t):
    N = list(map(int, input().split()))
    print(gcdf(N))