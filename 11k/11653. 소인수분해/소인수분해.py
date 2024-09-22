import math

def pf(x):
    for i in range(2, int(math.sqrt(n) + 1)):
        if x % i == 0:
            return i
    return x

n = int(input())

if n == 1:
    res = 1
else:
    while n > 1:
        print(pf(n))
        n = n // pf(n)