import math

def Euclidean(a, b):
    if b == 0:
        return a
    else:
        return Euclidean(b, a%b)

n = int(input())
P = []
arr = list(map(int, input().split()))
if n == 2:
    gcd = Euclidean(arr[0], arr[1])
    for i in range(1, int(math.sqrt(gcd)+1)):
        if gcd % i == 0:
            P.append(i)
            P.append(gcd // i)
    P = list(set(P))
    P.sort()
    for p in P:
        print(p)
else:
    gcd = Euclidean(arr[0], arr[1])
    gcd = Euclidean(gcd, arr[2])
    for i in range(1, int(math.sqrt(gcd)+1)):
        if gcd % i == 0:
            P.append(i)
            P.append(gcd // i)
    P = list(set(P))
    P.sort()
    for p in P:
        print(p)