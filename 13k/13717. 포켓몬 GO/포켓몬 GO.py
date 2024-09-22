import sys
input = sys.stdin.readline

def evf(a, b):
    cnt = 0
    while b >= a:
        b -= a
        cnt += 1
        b += 2
    return cnt

A = []
C = []
total = 0

n = int(input())
for _ in range(n):
    name = str(input())
    a, b = map(int, input().split())
    A.append(name)
    cnt = evf(a, b)
    C.append(cnt)
    total += cnt

inx = C.index(max(C))
print(total)
print(A[inx])