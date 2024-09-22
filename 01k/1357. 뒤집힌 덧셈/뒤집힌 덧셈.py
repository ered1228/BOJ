x, y = input().split()
x = str(x)
y = str(y)
x = x[::-1]
y = y[::-1]
x = int(x)
y = int(y)
res = x + y
res = str(res)
res = res[::-1]
print(int(res))