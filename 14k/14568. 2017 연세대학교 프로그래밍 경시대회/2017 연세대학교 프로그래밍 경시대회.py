n = int(input())
a = 0
b = 0
c = 0
cnt = 0

for i in range(2, n+1, 2):
    for j in range(1, n+1):
        for k in range(1, n+1):
            a = i
            b = j
            c = k
            if (a+b+c) == n and (b+2) <= c:
                cnt += 1
print(cnt)