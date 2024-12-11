n = int(input())
a, b, c, d = map(int, input().split())
h = str(input())

def f(h):
    for j in range(len(h)-1):
            if h[j] == h[j+1]:
                return False
    return True

if h[0] != 'a' or h[-1] != 'a':
    print("No")
else:
    ca = h.count('a')
    cb = h.count('b')
    cc = h.count('c')
    cd = h.count('d')
    if ca <= a and cb <= b and cc <= c and cd <= d:
        if f(h):
            print("Yes")
        else:
            print("No")
    else:
        print("No")