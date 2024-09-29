a, b, c = map(int, input().split())

def power(a, b, c):
    base = a
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * base) % c
        base = (base * base) % c
        b //= 2
    return res % c

print(power(a, b, c))