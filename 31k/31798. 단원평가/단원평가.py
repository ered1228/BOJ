a, b, c = map(int, input().split())
if a == 0:
    a = (c**2) - b
    r = a
elif b == 0:
    b = (c**2) - a
    r = b
elif c == 0:
    c = (a + b)**(1/2)
    r = int(c)
print(r)