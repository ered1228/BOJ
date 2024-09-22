a, b, c = map(int, input().split())
res1 = (a*b) / c
res2 = (a/b) * c
if res1 >= res2:
    print(int(res1))
else:
    print(int(res2))