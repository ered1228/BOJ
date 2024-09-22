n, h = map(int, input().split())
attack = list(map(int, input().split()))

s = 0
cnt = 0
for i in attack:
    s += i
    cnt += 1
    n -= 1
    if s >= h:
        print(cnt)
        break
    if n <= 0:
        print(-1)
        break