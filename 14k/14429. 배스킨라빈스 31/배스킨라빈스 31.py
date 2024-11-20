import sys
input = sys.stdin.readline

t = int(input())
C =[]
for i in range(t):
    j, m = map(int, input().split())
    r = (j-1) % (m+1)
    p = m+1
    cnt = 1
    while r+p < j:
        r += p
        cnt += 2
    cnt += 1
    C.append((i+1, cnt))

C.sort(key=lambda x : (x[1], x[0]))

print(C[0][0], C[0][1])