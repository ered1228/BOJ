def Euclidean(a, b):
    if b == 0:
        return a
    else:
        return Euclidean(b, a%b)
     
n, m = map(int, input().split())
if n == 1:
    print('1/{}'.format(m))
else:
    gcd = Euclidean(n, m)
    n = n // gcd
    m = m // gcd
    print('{}/{}'.format(n, m))