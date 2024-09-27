n, c = map(int, input().split())
cnt = 0
c = str(c)
for j in range(1, n+1):
    temp = str(j)
    cnt += temp.count(c)
print(cnt)