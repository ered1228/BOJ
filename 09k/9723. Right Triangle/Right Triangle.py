import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    T = list(map(int, input().split()))
    T.sort()
    hypotenuse = T[2]
    opposite = T[1]
    adjacent = T[0]
    if hypotenuse**2 == opposite**2 + adjacent**2:
        res = "YES"
    else:
        res = "NO"
    print(f"Case #{i+1}: {res}") 