import math

t = int(input())
cnt = 0
for _ in range(t):
    s = str(input())
    if s == s[::-1]:
        cnt += 1
if cnt < 2:
    print(0)
else:
    print(math.comb(cnt, 2) * 2)