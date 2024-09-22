from math import factorial

n, a, b, c = map(int, input().split())
r = factorial(n)
d = factorial(a) * factorial(b) * factorial(c)
print(r//d)