def Z(r, c, l, d):
    h = l//2
    if l == 2:
        if r == 0 and c == 0:
            return d
        elif r == 0 and c == 1:
            return d+1
        elif r == 1 and c == 0:
            return d+2
        else:
            return d+3    
    else:
        if r < h and c < h:
            return Z(r, c, h, d)
        elif r < h and c >= h:
            return Z(r, c-h, h, d+(h**2))
        elif r >= h and c < h:
            return Z(r-h, c, h, d+((h**2)*2))
        elif r >= h and c >= h:
            return Z(r-h, c-h, h, d+((h**2)*3))

n, r, c = map(int, input().split())
l = 2**n
print(Z(r, c, l, 0))