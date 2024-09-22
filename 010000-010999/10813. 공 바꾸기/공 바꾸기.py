n, m = map(int, input().split())
bk = [a for a in range(1, n+1)]
c = 0

for b in range(m):
    i, j = map(int, input().split())
    c = bk[i-1]
    bk[i-1] = bk[j-1]
    bk[j-1] = c

for com in bk:
    print(com, end=" ")