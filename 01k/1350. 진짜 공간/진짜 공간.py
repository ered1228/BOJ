n = int(input())
A = list(map(int, input().split()))
c = int(input())

cnt = 0
for a in A:
    if a <= c:
        cnt += 1
    else:
        if (a % c) == 0:
            cnt += a // c
        else:
            cnt += a // c + 1

cnt -= A.count(0)
print(cnt * c)