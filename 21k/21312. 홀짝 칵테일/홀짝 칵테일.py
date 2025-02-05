def odd(n):
    if n % 2 == 1:
        return -1
    return 0

a, b, c = map(int, input().split())
f = [a, b, c, a*b, a*c, b*c, a*b*c]
f.sort(key=lambda x: (odd(x), -x))
print(f[0])