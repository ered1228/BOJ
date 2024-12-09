a, b = map(int, input().split())
c, d = map(int, input().split())
e, f, g = map(int, input().split())
res = e*f*g
res *= (a*b) + (c*d)
print(res)