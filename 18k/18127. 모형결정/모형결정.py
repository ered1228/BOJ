a, b = map(int, input().split())
res = 0
temp = 1
for i in range(b+1):
    res += temp
    temp += a-2
print(res)