a, b, v = map(int, input().split())
temp = (v - b) % (a - b)
if temp == 0:
    print((v - b)//(a - b))
else:
    print((v - b)//(a - b) + 1)