import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    r1 = (a+b)**2 + c**2
    r2 = (b+c)**2 + a**2
    r3 = (c+a)**2 + b**2
    print(min(r1, r2, r3))