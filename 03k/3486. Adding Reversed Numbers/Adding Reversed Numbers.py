t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a = str(a) ; b = str(b)
    a = a[::-1]
    b = b[::-1]
    a = int(a) ; b = int(b)
    print(int(str(a+b)[::-1]))