def s(a):
    result = 0
    result = a**2
    return result
a, b, c, d, e = map(int, input().split())
print((s(a)+s(b)+s(c)+s(d)+s(e))%10)