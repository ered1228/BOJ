x, y, w, h = map(int, input().split())
if (w/2) >= x:
    dx = x
    if (h/2) >= y:
        dy = y
        if dx >= dy:
            d = dy
        else:
            d = dx
    if y > (h/2):
        dy = h - y
        if dx >= dy:
            d = dy
        else:
            d = dx
elif x > w/2:
    dx = w - x
    if (h/2) >= y:
        dy = y
        if dx >= dy:
            d = dy
        else:
            d = dx
    if y > (h/2):
        dy = h - y
        if dx >= dy:
            d = dy
        else:
            d = dx
print(d)