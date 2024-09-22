t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    F = n % h
    R = (n // h) + 1
    if F == 0:
        F = h
        R -= 1
    print(F*100 + R)