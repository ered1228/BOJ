x, y = input().split()
j1 = x.isdecimal()
j2 = y.isdecimal()

if not j1:
    print("NaN")
elif not j2:
    print("NaN")
else:
    res = int(x) - int(y)
    print(res)