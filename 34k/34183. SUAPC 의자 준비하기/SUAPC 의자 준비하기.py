n, m, a, b = map(int, input().split())
chair = 3*n - m
if chair <= 0:
    print(0)
else:
    print(chair*a + b)