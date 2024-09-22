import sys
input = sys.stdin.readline

def Euclidean(a, b):
    if b == 0:
        return a
    else:
        return Euclidean(b, a%b)

a, b = map(int, input().split())
gcd = Euclidean(a, b)
print(gcd * (a // gcd) * (b // gcd))