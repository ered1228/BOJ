import math

a, b = map(int, input().split())
if (a, b) == (0, 0):
    print(0)
elif math.gcd(a, b) == 1:
    print(1)
else:
    print(2)