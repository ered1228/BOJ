import sys
input = sys.stdin.readline

def Euclidean(a, b):
    if b == 0:
        return a
    else:
        return Euclidean(b, a%b)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    gcd = Euclidean(a, b)
    lcm = (a//gcd) * (b//gcd) * (gcd)
    print(lcm, gcd)