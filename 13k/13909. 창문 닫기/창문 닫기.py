n = int(input())
m = 10000
if m**2 > n:
    while m**2 > n:
        m -= 1
    print(m)
elif m**2 == n:
    print(m)
else:
    while m**2 <= n:
        m += 1
    print(m-1)